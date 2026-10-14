"""Append one LinkedIn post (from workflow inputs in env vars) to posts.json."""
import datetime
import json
import os
import re
import sys

PATH = "posts.json"

url = os.environ["P_URL"].strip()
if not re.match(r"^https://([a-z]+\.)?linkedin\.com/", url):
    sys.exit(f"Not a LinkedIn link: {url}")
url = url.split("?")[0]  # drop tracking parameters

date = os.environ.get("P_DATE", "").strip() or datetime.date.today().isoformat()
try:
    datetime.date.fromisoformat(date)
except ValueError:
    sys.exit(f"Date must be YYYY-MM-DD, got: {date}")

with open(PATH, encoding="utf-8") as f:
    posts = json.load(f)

if any(p.get("url") == url for p in posts):
    print("This post is already on the website.")
    sys.exit(0)

posts.insert(0, {
    "title": os.environ["P_TITLE"].strip(),
    "summary": os.environ["P_SUMMARY"].strip(),
    "category": os.environ["P_CATEGORY"].strip(),
    "tags": [t.strip() for t in os.environ.get("P_TAGS", "").split(",") if t.strip()],
    "source": "linkedin",
    "date": date,
    "url": url,
})

with open(PATH, "w", encoding="utf-8") as f:
    json.dump(posts, f, indent=2, ensure_ascii=False)
    f.write("\n")

print(f"Added: {posts[0]['title']}")
