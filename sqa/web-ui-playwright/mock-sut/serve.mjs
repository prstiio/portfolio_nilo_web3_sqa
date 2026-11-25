// Tiny static server for the local mock SUT. Not the real SauceDemo.
// Any path without a file extension falls back to index.html (SPA routing).
import { createServer } from 'node:http';
import { readFile } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';

const dir = dirname(fileURLToPath(import.meta.url));
const port = Number(process.env.MOCK_PORT ?? 4173);

createServer(async (_req, res) => {
  try {
    const html = await readFile(join(dir, 'index.html'));
    res.writeHead(200, { 'content-type': 'text/html; charset=utf-8' });
    res.end(html);
  } catch (err) {
    res.writeHead(500);
    res.end(String(err));
  }
}).listen(port, () => console.log(`Mock SUT on http://localhost:${port}`));
