import rss from '@astrojs/rss';
import { SITE } from '../data/topics';
import { excerpt, getPosts, postUrl } from '../data/posts';

export async function GET(context) {
  const posts = await getPosts();
  return rss({
    title: SITE.title,
    description: SITE.description,
    site: context.site,
    items: posts.map((p) => ({
      title: p.data.title,
      description: excerpt(p, 300),
      pubDate: p.data.date,
      link: postUrl(p),
      categories: p.data.tags,
    })),
  });
}
