# Web3 / smart-contract testing (optional differentiator)

Templates for testing contracts on **local or testnet only**. No mainnet interaction, no attacks on live protocols (see [SECURITY.md](../../SECURITY.md)).

| File | Purpose |
|---|---|
| `test-plan.md` | What to test and with which technique |
| `threat-model.md` | Assets, actors, trust assumptions, attack surfaces |
| `findings.md` | Finding template (proof of concept required before a finding counts) |
| `triage.md` | Static-analysis output triage table |

## Technique map
| Technique | Tool | Answers |
|---|---|---|
| Unit tests | Foundry (`forge test`) | Does each function behave as specified? |
| Fuzz tests | Foundry fuzzing | Does it hold for inputs I did not think of? |
| Invariant tests | Foundry invariants | Do global properties (e.g. total supply = sum of balances) always hold? |
| Fork tests | Foundry fork mode (read-only RPC) | Does it behave against real deployed state? |
| Static analysis | Slither | Which patterns need a human look? Output is a lead, not a finding |

## Rules
1. A finding needs a reproducible PoC on a local fork or testnet. A tool warning alone is not a finding.
2. Report privately to the owner or program first; never publish unfixed issues.
3. Severity follows the program's rubric; yours goes in the `Severity rationale` field.
4. Status: TODO. Nothing here has been run yet.
