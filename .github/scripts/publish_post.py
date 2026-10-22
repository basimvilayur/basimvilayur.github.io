"""Publish a "New post" issue: optionally post it to LinkedIn, then add it to the website."""
import datetime
import json
import os
import re
import sys
import urllib.error
import urllib.request

from postfile import CATEGORIES, existing, write_post

# LinkedIn REST API version (YYYYMM). Each version is supported for about a year; bump it then.
LINKEDIN_VERSION = "202609"


def parse_issue_form(body):
    """Issue forms render as '### Label' followed by the answer."""
    fields, label = {}, None
    for line in (body or "").splitlines():
        m = re.match(r"^### (.+)$", line)
        if m:
            label = m.group(1).strip()
            fields[label] = []
        elif label:
            fields[label].append(line)
    out = {k: "\n".join(v).strip() for k, v in fields.items()}
    return {k: ("" if v == "_No response_" else v) for k, v in out.items()}


def to_little(text):
    """Escape LinkedIn 'little' reserved characters, keeping plain #hashtags working."""
    text = re.sub(r"([\\|{}@\[\]()<>*_~])", r"\\\1", text)
    return re.sub(r"#(?!\w)", r"\\#", text)


def linkedin(method, url, token, body=None):
    req = urllib.request.Request(url, method=method, data=json.dumps(body).encode() if body else None)
    req.add_header("Authorization", f"Bearer {token}")
    req.add_header("LinkedIn-Version", LINKEDIN_VERSION)
    req.add_header("X-Restli-Protocol-Version", "2.0.0")
    req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.status, dict(r.headers), r.read().decode() or "{}"
    except urllib.error.HTTPError as e:
        detail = e.read().decode(errors="replace")
        if e.code == 401:
            sys.exit("LinkedIn token is invalid or expired (they last 60 days). "
                     "Create a new one and update the LINKEDIN_TOKEN secret. " + detail)
        sys.exit(f"LinkedIn API error {e.code}: {detail}")


def post_to_linkedin(text, token):
    _, _, info = linkedin("GET", "https://api.linkedin.com/v2/userinfo", token)
    person = json.loads(info)["sub"]
    status, headers, _ = linkedin("POST", "https://api.linkedin.com/rest/posts", token, {
        "author": f"urn:li:person:{person}",
        "commentary": to_little(text),
        "visibility": "PUBLIC",
        "distribution": {"feedDistribution": "MAIN_FEED", "targetEntities": [], "thirdPartyDistributionChannels": []},
        "lifecycleState": "PUBLISHED",
        "isReshareDisabledByAuthor": False,
    })
    urn = {k.lower(): v for k, v in headers.items()}.get("x-restli-id")
    if status != 201 or not urn:
        sys.exit(f"LinkedIn did not confirm the post (status {status}).")
    return f"https://www.linkedin.com/feed/update/{urn}/"


def main():
    with open(os.environ["GITHUB_EVENT_PATH"], encoding="utf-8") as f:
        issue = json.load(f)["issue"]
    form = parse_issue_form(issue["body"])

    title = issue["title"].strip()
    text = form.get("Post text", "")
    category = form.get("Topic", "")
    tags = [t.strip() for t in form.get("Tags", "").split(",") if t.strip()]
    to_li = form.get("Also post on LinkedIn?", "Yes") == "Yes"

    if not text:
        sys.exit("Post text is empty.")
    if category not in CATEGORIES:
        sys.exit(f"Unknown topic: {category!r}")
    if not title or title == "Post title here":
        sys.exit("Please give the issue a real title (it becomes the website card title).")

    if existing("issue", issue["number"]):
        print("Already published; nothing to do.")
        return

    url = ""
    if to_li:
        token = os.environ.get("LINKEDIN_TOKEN", "").strip()
        if not token:
            sys.exit("LINKEDIN_TOKEN secret is not set. Add it, or choose 'No' for LinkedIn.")
        url = post_to_linkedin(text, token)
        print(f"Posted on LinkedIn: {url}")
        with open(os.environ["GITHUB_OUTPUT"], "a", encoding="utf-8") as out:
            out.write(f"linkedin_url={url}\n")

    # Markdown joins single lines; a trailing double space keeps LinkedIn's line breaks.
    body = re.sub(r"(?<!\n)\n(?!\n)", "  \n", text)
    path = write_post(
        title=title,
        date=datetime.date.today().isoformat(),
        category=category,
        body=body,
        tags=tags,
        linkedin=url,
        issue=issue["number"],
    )
    print(f"Added to website: {path}")


if __name__ == "__main__":
    main()
