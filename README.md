# basimvilayur.github.io

Source for https://www.basimvilayur.com

## Publishing a new post (website + LinkedIn in one go)

Open https://github.com/basimvilayur/basimvilayur.github.io/issues/new?template=new-post.yml
(or in the GitHub app: **Issues → New → New post**), then:

- **Title** → the website card title
- **Post text** → written exactly as it should appear on LinkedIn (line breaks and #hashtags kept)
- **Topic**, **Tags**, and **Also post on LinkedIn?**

Submit. Within about a minute the post is on LinkedIn and the website, and the issue is
closed with both links. If something fails, the issue gets a comment explaining why;
fix it and **Reopen** the issue to retry. Only issues you open yourself are published.

### One-time LinkedIn setup

1. https://www.linkedin.com/developers/apps → **Create app**. LinkedIn requires the app to
   be linked to a LinkedIn Page you admin; posts still go to your personal profile.
2. In the app: **Products** → add **Share on LinkedIn** and
   **Sign In with LinkedIn using OpenID Connect**.
3. **Auth** tab → under *Authorized redirect URLs* add
   `https://www.linkedin.com/developers/tools/oauth/redirect`.
4. Get a token (see below) and save it as the `LINKEDIN_TOKEN` secret.

### Renew LinkedIn token (every 60 days)

1. https://www.linkedin.com/developers/tools/oauth/token-generator → pick the app,
   tick `openid`, `profile`, `w_member_social` → **Request access token** → sign in → copy it.
2. Repo **Settings → Secrets and variables → Actions** → `LINKEDIN_TOKEN` → paste → save.

A weekly check opens a reminder issue when the token stops working.

## Adding a post you already made on LinkedIn

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
