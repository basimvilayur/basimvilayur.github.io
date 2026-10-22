import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://basimvilayur.com',
  trailingSlash: 'always',
  compressHTML: true,
  integrations: [sitemap()],
});
