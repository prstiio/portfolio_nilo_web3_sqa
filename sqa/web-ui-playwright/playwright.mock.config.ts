import { defineConfig, devices } from '@playwright/test';

// Runs the SAME suite against the bundled local mock (mock-sut/), not the real SauceDemo.
// A green run here proves the framework logic works; it says nothing about the real site.
const MOCK_PORT = Number(process.env.MOCK_PORT ?? 4173);
const MOCK_URL = `http://localhost:${MOCK_PORT}`;

export default defineConfig({
  testDir: './tests',
  fullyParallel: true,
  timeout: 30_000,
  expect: { timeout: 5_000 },
  reporter: [['list'], ['json', { outputFile: 'test-results/results.json' }]],
  use: {
    baseURL: MOCK_URL,
    testIdAttribute: 'data-test',
    trace: 'on-first-retry',
    screenshot: 'only-on-failure',
  },
  webServer: {
    command: 'node mock-sut/serve.mjs',
    url: MOCK_URL,
    env: { MOCK_PORT: String(MOCK_PORT) },
    reuseExistingServer: !process.env.CI,
    timeout: 15_000,
  },
  projects: [{ name: 'chromium', use: { ...devices['Desktop Chrome'] } }],
});
