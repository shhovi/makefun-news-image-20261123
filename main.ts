// news-image-20261123 — run-time half of the entry.
//
// entry.png (the 23 November 2026 world-news poster) is drawn at build
// time by draw_image.py and committed beside this file. The poster sums
// up Monday 23 November 2026: COP31 collapsing in Antalya, Ukraine
// sinking the Russian corvette Merkury off Libya, Nvidia reinstating
// Jensen Huang as CEO with US stocks rebounding, and the Democrats
// clinching a record House majority. The grader runs this program with
// no network: it checks the PNG header against the gate limits
// (1024x1024, 1 MiB) and writes the bytes to the output directory,
// /output unless MAKEFUN_OUTPUT_DIR says otherwise.
//
// Local check:  mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, mkdirSync, readFileSync, statSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const LIMIT_BYTES = 1024 * 1024;
const LIMIT_EDGE = 1024;

const here = dirname(fileURLToPath(import.meta.url));
const source = join(here, 'entry.png');

const { size } = statSync(source);
if (size === 0) {
  throw new Error('entry.png is empty');
}
if (size > LIMIT_BYTES) {
  throw new Error(`entry.png weighs ${size} bytes; the gate allows ${LIMIT_BYTES}`);
}

const head = readFileSync(source).subarray(0, 24);
const PNG_MAGIC = [137, 80, 78, 71, 13, 10, 26, 10];
const isPng = PNG_MAGIC.every((byte, i) => head[i] === byte);
if (!isPng) {
  throw new Error('entry.png does not start with the PNG signature');
}
const width = head.readUInt32BE(16);
const height = head.readUInt32BE(20);
if (width > LIMIT_EDGE || height > LIMIT_EDGE) {
  throw new Error(`entry.png is ${width}x${height}; the gate allows ${LIMIT_EDGE}x${LIMIT_EDGE}`);
}

const target = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
mkdirSync(target, { recursive: true });
copyFileSync(source, join(target, 'entry.png'));
console.log(`copied entry.png (${width}x${height}, ${size} bytes) to ${target}`);
