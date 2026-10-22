"""Shared helpers for writing website posts as Markdown files in src/content/posts/."""
import glob
import json
import os
import re

POSTS_DIR = "src/content/posts"
CATEGORIES = {"networking", "servers", "security", "cloud", "odoo", "automation", "database", "interviews"}


def slugify(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")[:70].strip("-") or "post"


def existing(field, value):
    """True if any post's front matter has `field: value` (value compared as JSON)."""
    needle = re.compile(rf"^{field}:\s*{re.escape(json.dumps(value))}\s*$", re.M)
    for path in glob.glob(os.path.join(POSTS_DIR, "*.md")):
        with open(path, encoding="utf-8") as f:
            head = f.read().split("\n---", 1)[0]
        if needle.search(head):
            return True
    return False


def write_post(title, date, category, body, summary="", tags=(), linkedin="", issue=None):
    """Write a new post file and return its path. JSON strings are valid YAML, so values are safely quoted."""
    if category not in CATEGORIES:
        raise SystemExit(f"Unknown topic: {category!r}")
    q = lambda v: json.dumps(v, ensure_ascii=False)
    lines = ["---", f"title: {q(title)}", f"summary: {q(summary)}", f"date: {date}",
             f"category: {category}", f"tags: {q(list(tags))}"]
    if linkedin:
        lines.append(f"linkedin: {q(linkedin)}")
    if issue is not None:
        lines.append(f"issue: {int(issue)}")
    lines.append("---")

    base = slugify(title)
    path, n = os.path.join(POSTS_DIR, f"{base}.md"), 2
    while os.path.exists(path):
        path, n = os.path.join(POSTS_DIR, f"{base}-{n}.md"), n + 1

    os.makedirs(POSTS_DIR, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines) + "\n\n" + body.strip() + "\n")
    return path
