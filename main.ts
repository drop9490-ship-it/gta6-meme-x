// gta6-meme-x-01 — main.ts
// Copies POST.json from the repository root to /output/POST.json.
// That is all it has to do: the post itself is the entry, the house
// reads it from X. Standard library only, no network, deterministic:
// the same input bytes always produce the same output bytes.
import { copyFileSync, existsSync, mkdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const scriptDir: string = dirname(fileURLToPath(import.meta.url));
const candidates: string[] = [
  join(scriptDir, "POST.json"),
  join(process.cwd(), "POST.json"),
];

const source: string | undefined = candidates.find((p: string) =>
  existsSync(p),
);
if (source === undefined) {
  throw new Error(
    "POST.json not found next to main.ts or in the working directory",
  );
}

mkdirSync("/output", { recursive: true });
copyFileSync(source, "/output/POST.json");
console.log("copied POST.json to /output/POST.json");
