# Thinking Logs

Three habits, one small file each. Total time: about 15 minutes per week. They turn "I worked hard" into evidence you can show.

| Mode | Question it answers | File | Weekly action |
|---|---|---|---|
| **Strategic** | What deserves my limited time? | [`decision-log.md`](decision-log.md), `sqa/01-planning/03-risk-assessment.md` | Re-score top risks; log any decision that changes scope or tools |
| **Metacognitive** | How reliable is my own judgment, and when do I over-trust AI? | [`confidence-log.csv`](confidence-log.csv) | Log predictions before verifying; compute calibration monthly |
| **Critical** | Is each claim backed by evidence? | [`evidence-register.md`](evidence-register.md), `sqa/ai-testing/verification-gate.md` | Ask the five questions below before publishing any number or conclusion |

## Five critical questions
1. What is the evidence (a command, a run, a file) rather than a feeling or an AI statement?
2. What other explanation fits the same data?
3. What does this test **not** cover?
4. What would change my mind?
5. Who is harmed if this is wrong, and is my verification proportional?

## Why these habits (evidence)
- Generative AI shifts effort from producing to verifying and supervising, and loading users with metacognitive demands (judging output, deciding what to automate) — Tankelevitch et al., CHI '24 (Microsoft Research).
- In a survey of 319 knowledge workers, higher confidence in AI went with less self-reported critical thinking (β = −0.69), while higher self-confidence went with more (β = 0.26). The data are self-reported perceptions — Lee et al., CHI '25 (Microsoft Research / Carnegie Mellon).
- OpenAI argues models guess because common evaluations reward guessing over admitting uncertainty, so confident wrong answers are expected behavior to guard against — OpenAI, "Why language models hallucinate", 5 Sep 2025.

Full references: see the learning material that accompanies this repository.

## Confidence log format
`docs/thinking/confidence-log.csv`, one row per AI-assisted judgment. Columns: `date` (YYYY-MM-DD) · `task` · `delegated_to_ai` (yes/no) · `prediction` (`correct`/`incorrect`: your guess about the AI output before verifying) · `confidence_pct` (0–100) · `verified_result` (`correct`/`incorrect`) · `match` (`yes`/`no`) · `lesson`.
`python scripts/portfolio_status.py` prints calibration once there are at least 10 rows: for stated confidence ≥ 80%, how often were you right?
