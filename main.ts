// news-image-20261124 entry (Node 22, standard library only).
//
// The entry image is entry.png beside this file: a one-page newspaper
// front page summing up the world news of Tuesday 24 November 2026,
// drawn programmatically by draw.py (committed beside it) so every word
// stays crisp. This program's whole job is to place those exact bytes
// at /output/entry.png, deterministically, with no network.
//
// Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for
// /output:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync } from 'node:fs';
import { join } from 'node:path';

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
const source = new URL('./entry.png', import.meta.url);

copyFileSync(source, join(outDir, 'entry.png'));
