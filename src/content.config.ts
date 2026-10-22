import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';
import { TOPIC_IDS } from './data/topics';

const posts = defineCollection({
  loader: glob({ base: './src/content/posts', pattern: '**/*.md' }),
  schema: z.object({
    // The browser editor may save empty fields as null, so optional fields accept null too.
    title: z.string(),
    summary: z.string().nullish().transform((v) => v ?? ''),
    date: z.coerce.date(),
    category: z.enum(TOPIC_IDS),
    tags: z.array(z.string()).nullish().transform((v) => v ?? []),
    linkedin: z.string().url().or(z.literal('')).nullish().transform((v) => v || ''),
    draft: z.boolean().nullish().transform((v) => v ?? false),
    issue: z.number().nullish(),
  }),
});

export const collections = { posts };
