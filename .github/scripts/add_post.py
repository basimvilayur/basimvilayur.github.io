"""Add a post already made on LinkedIn (from workflow inputs in env vars) as a website post."""
import datetime
import os
import re
import sys
import urllib.request

from postfile import existing, write_post

LINKEDIN = r"^https://([a-z]+\.)?linkedin\.com/"

url = os.environ["P_URL"].strip()
if re.match(r"^https://lnkd\.in/", url):
    # Short share link: follow it to the full linkedin.com post URL.
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=20) as r:
            if re.match(LINKEDIN, r.geturl()):
                url = r.geturl()
    except OSError as e:
        print(f"Could not expand short link, keeping it as is: {e}")
elif not re.match(LINKEDIN, url):
    sys.exit(f"Not a LinkedIn link: {url}")
url = url.split("?")[0]  # drop tracking parameters

date = os.environ.get("P_DATE", "").strip() or datetime.date.today().isoformat()
try:
    datetime.date.fromisoformat(date)
except ValueError:
    sys.exit(f"Date must be YYYY-MM-DD, got: {date}")

if existing("linkedin", url):
    print("This post is already on the website.")
    sys.exit(0)

text = os.environ.get("P_SUMMARY", "").strip()
body = text or "I shared this on LinkedIn — read the full post and join the discussion there."
path = write_post(
    title=os.environ["P_TITLE"].strip(),
    date=date,
    category=os.environ["P_CATEGORY"].strip(),
    body=body,
    tags=[t.strip() for t in os.environ.get("P_TAGS", "").split(",") if t.strip()],
    linkedin=url,
)
print(f"Added: {path}")
