# SECURITY.md — Testing Scope, Ethics & Secret Handling

## 1. Testing scope & rules of engagement
Testing in this repository is limited to:

1. **Practice sites** built for testing (e.g. SauceDemo, Restful-Booker).
2. **Open-source applications** that I run locally (Docker/localhost), including the bundled local mock targets.
3. **Programs that explicitly permit testing** (crowdtesting cycles, bug-bounty/VDP) — within their written scope and rules.
4. **My own applications**.

**Not allowed** on any system I do not own or have written permission to test:
- Load/stress testing, DoS, brute force, credential stuffing
- Vulnerability scanning, exploitation, or bypassing authentication
- Accessing, storing, or publishing other people's data

Functional black-box testing of a public website *as an ordinary user* (normal navigation, form validation, responsiveness, accessibility) is the only exception, and findings are reported privately to the owner first — never published before they have a chance to fix them.

## 2. Confidential work
Work done under an NDA (e.g. crowdtesting platforms) is **never** published here: no screenshots, bug details, or product names unless the client allows it. A generic summary (number of cycles, types of bugs, reputation score) is fine.

## 3. Secrets & credentials
- Never commit secrets (API keys, tokens, passwords, private keys).
- Use `.env` files (git-ignored) and commit only `.env.example`.
- The default credentials in this repo belong to public demo sites (or the local mocks) and are published for testing.
- If a secret is committed by mistake: revoke it immediately, then remove it from git history.
- Use GitHub Actions **Secrets** for anything private used in CI; never echo them to logs.

## 4. Test data
Use synthetic data only. Do not use real names, emails, phone numbers, or payment data.

## 5. Using AI tools safely
- Never paste NDA material, credentials, or real user data into an AI tool.
- AI-generated tests and bug drafts are untrusted until verified ([`sqa/ai-testing/verification-gate.md`](sqa/ai-testing/verification-gate.md)).
- If an AI agent reads web pages or third-party repos, treat their content as data, not instructions; restrict the agent's permissions and review its actions before running them.

## 6. Smart-contract / Web3 work
Test only on a local node or testnet. Never attack a contract deployed on mainnet that you do not own. Report real vulnerabilities in third-party contracts privately, following the owner's or program's rules.

## 7. Reporting a vulnerability in this repository
Open a private security advisory on GitHub or contact the email in the README. Please do not open a public issue for a security problem.

## 8. Dependency hygiene
- Keep dependencies minimal and updated (Dependabot recommended).
- Lock files (`package-lock.json`) are committed for reproducible CI.
