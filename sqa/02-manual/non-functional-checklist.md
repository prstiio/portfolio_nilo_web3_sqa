# Non-functional Checklist

Basic checks you can do without harming the target. Record **real** results; status stays `Not Run` until executed. Only test targets allowed by [`../SECURITY.md`](../../SECURITY.md) — no load tests, scans, or brute force on third-party systems.

Link measurable items to `NFR-*` requirements in [`../sqa/01-planning/01-requirements.md`](../01-planning/01-requirements.md).

## Accessibility (WCAG POUR: perceivable, operable, understandable, robust)
| Check | How | Pass criterion | Result | Notes |
|---|---|---|---|---|
| Keyboard only | Complete login and checkout with Tab / Shift+Tab / Enter / Space | Every control reachable and usable | Not Run | |
| Visible focus | Tab through the page | Focus indicator always visible | Not Run | |
| Form labels | Inspect inputs; try a screen reader briefly | Each input has a meaningful accessible name | Not Run | |
| Contrast | Contrast checker on text and buttons | Normal text ≥ 4.5:1 (WCAG AA) | Not Run | |
| Text alternatives | Inspect meaningful images | Informative `alt` present | Not Run | |
| Zoom / reflow | Zoom to 200%; width ≈ 412 px | Content not cut off; flows still usable | Not Run | |

## Performance (basic)
| Check | Tool | Record | Result | Notes |
|---|---|---|---|---|
| Page speed | Lighthouse in DevTools, 2 pages | LCP, CLS, TBT, date, throttling used | Not Run | |
| API response time | Time 5 endpoints × 20 calls in a script | Median and p95 (not only the mean) | Not Run | |
| Load / stress | **Only** on your own system or with written permission | — | Not Run | |

## Security awareness (safe, black-box, ordinary-user level)
| Check | Safe example | Result | Notes |
|---|---|---|---|
| Auth required | Open a protected URL after logout | Not Run | |
| Object-level access | On your own local app: can user A fetch user B's record by changing an id? | Not Run | |
| Input handling | Quotes and HTML tags entered as plain text are handled safely | Not Run | |
| Sensitive data | No passwords/tokens in URL, logs, or responses | Not Run | |
| Session end | Back button after logout does not restore access | Not Run | |

## Compatibility
| Check | Environment | Result | Notes |
|---|---|---|---|
| Core flows | Chromium, Firefox, WebKit | Not Run | |
| Mobile viewport | Pixel 7 emulation / 412×915 | Not Run | |
