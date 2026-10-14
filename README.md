# basimvilayur.github.io

Source for https://www.basimvilayur.com

## Adding a LinkedIn post to the website

1. On LinkedIn, open your post → **⋯ → Copy link to post**.
2. On GitHub (web or mobile app): **Actions → Add LinkedIn post to website → Run workflow**.
3. Paste the link, a short title, the post text, pick a topic, and run.

The workflow adds the post to `posts.json` and the site updates in about a minute.
Posting the same link twice is ignored.

## Editing posts by hand

All posts and notes live in `posts.json`. Each entry:

```json
{
  "title": "Card title",
  "summary": "2-3 line description",
  "category": "networking | servers | security | cloud | odoo | automation | database | interviews",
  "tags": ["Tag1", "Tag2"],
  "source": "linkedin | note",
  "date": "YYYY-MM-DD",
  "url": "https://..."
}
```

Newest dated entries show first.
