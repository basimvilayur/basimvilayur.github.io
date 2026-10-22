import { getCollection, type CollectionEntry } from 'astro:content';

export type Post = CollectionEntry<'posts'>;

/** Published posts, newest first. */
export async function getPosts(): Promise<Post[]> {
  const posts = await getCollection('posts', (p) => !p.data.draft);
  return posts.sort((a, b) => b.data.date.valueOf() - a.data.date.valueOf());
}

export function postUrl(p: Post) {
  return `/posts/${p.id}/`;
}

export function formatDate(d: Date) {
  return d.toLocaleDateString('en-GB', { day: 'numeric', month: 'short', year: 'numeric', timeZone: 'UTC' });
}

export function readingTime(p: Post) {
  const words = (p.body ?? '').split(/\s+/).filter(Boolean).length;
  return Math.max(1, Math.round(words / 220));
}

/** Card text: the summary, or the start of the body when there is none. */
export function excerpt(p: Post, max = 220) {
  const text = (p.data.summary || (p.body ?? '').replace(/[#*_>`\[\]()]/g, '')).replace(/\s+/g, ' ').trim();
  return text.length > max ? text.slice(0, max).replace(/\s+\S*$/, '') + '…' : text;
}
