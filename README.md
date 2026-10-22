# basimvilayur.github.io

Source for https://basimvilayur.com, built with [Astro](https://astro.build) and deployed to
GitHub Pages by the **Deploy website** workflow on every push to `main`.

Pages: home, `/posts/` (searchable list), `/posts/<name>/` (one page per post), `/topics/`,
`/topics/<topic>/`, `/about/`, plus `/rss.xml` and a sitemap.

Every post is a Markdown file in `src/content/posts/`.

## Writing and editing posts in the browser (Pages CMS)

1. Go to https://app.pagescms.org and sign in with GitHub (as `basimvilayur`).
2. Open this repository → **Posts**. Add a new post or edit an existing one with the visual editor,
   upload images, and save. Saving commits to `main`, and the site updates in about a minute.

Tick **Draft** to keep a post off the website while you work on it.

## Publishing a new post to LinkedIn and the website in one go

Open https://github.com/basimvilayur/basimvilayur.github.io/issues/new?template=new-post.yml
(or in the GitHub app: **Issues → New → New post**), then:

- **Title** → the website post title
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
2. On GitHub: **Actions → Add LinkedIn post to website → Run workflow**.
3. Paste the link, a short title, the post text, pick a topic, and run.

Posting the same link twice is ignored.

## Post file format

```markdown
---
title: "Post title"
date: 2026-10-22
category: servers        # networking | servers | security | cloud | odoo | automation | database | interviews
tags: ["Proxmox", "Backup"]
summary: ""              # optional; card text (defaults to the start of the post)
linkedin: ""             # optional; link to the LinkedIn version
draft: false
---

The post itself, in Markdown.
```

The file name becomes the page address: `proxmox-backup.md` → `/posts/proxmox-backup/`.

## Working on the site locally

```bash
npm install
npm run dev
```
