// Entry point for the news-image-20261123 bounty (Node 22, stdlib only).
//
// The poster is drawn ahead of time by draw_image.py and ships in this
// repository as entry.png (1024x1024). All this program does is place a
// copy of it where the grader looks: MAKEFUN_OUTPUT_DIR/entry.png, or
// /output/entry.png when that variable is not set.
//
// Local run:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

// The repository root is the folder this file lives in.
const repoRoot = dirname(fileURLToPath(import.meta.url));
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
const sourcePath = join(repoRoot, "entry.png");
const targetPath = join(outDir, "entry.png");

const pixels = readFileSync(sourcePath);
mkdirSync(outDir, { recursive: true });
writeFileSync(targetPath, pixels);

// Confirm the copy landed intact: same bytes, same size.
if (!readFileSync(targetPath).equals(pixels)) {
  throw new Error("entry.png did not copy cleanly to " + targetPath);
}
