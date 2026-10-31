# F1 Aerodynamics Assessment Prep

A self-study revision guide for an F1 aerodynamics internship assessment (prepared with Red Bull Racing's process in mind). It builds from basic fluid mechanics up to F1-specific aero, the 2026 regulations, CFD, wind tunnel correlation, data skills and interview prep.

**Start here: [revision-guide.md](revision-guide.md)**

## What's inside

| Path | What it is |
| --- | --- |
| [`revision-guide.md`](revision-guide.md) | The full guide: 15 parts, worked examples, "Check yourself" questions and a final checklist |
| [`scripts/cla_vs_ride_height.py`](scripts/cla_vs_ride_height.py) | Runnable version of the Part 11 Python workflow: C_L·A against ride height with 95% confidence intervals |
| `requirements.txt` | Python dependencies for the script |

## Guide contents

| Part | Topic |
| --- | --- |
| 1 | Fluid fundamentals: pressure, Bernoulli, continuity, momentum, Reynolds number |
| 2 | Forces, coefficients and aero balance |
| 3 | Boundary layers, separation, wings and diffusers |
| 4 | Vortices and flow structures |
| 5 | Anatomy of an F1 car, component by component |
| 6 | The 2026 regulations and active aero (X-mode and Z-mode) |
| 7 | Sensitivities, porpoising, wake and following cars |
| 8 | From aero to lap time |
| 9 | CFD in practice: turbulence models, meshing, y+, convergence |
| 10 | Wind tunnel testing and correlation |
| 11 | Data and coding skills: C_p plots, total-pressure maps, Python |
| 12 | Red Bull context and how to talk about it honestly |
| 13 | 13 practice questions with worked answers |
| 14 | Non-technical prep: STAR stories, project pitch, questions to ask |
| 15 | Seven-day study plan, reading list and final checklist |

## How to study

1. Read a part once, then close it and explain the main idea aloud in 60 seconds.
2. Redo every worked calculation by hand.
3. Answer the "Check yourself" questions before reading the answers in Part 13.
4. Note anything you can't explain simply. That is where an interviewer will probe.

## Running the script

```bash
pip install -r requirements.txt
python scripts/cla_vs_ride_height.py          # generates synthetic runs.csv if none exists
python scripts/cla_vs_ride_height.py my.csv   # or use your own data
```

Your CSV needs the columns `speed_ms`, `rho`, `ride_mm` and `downforce_N`. The script prints a summary table and saves `cla_vs_ride_height.png`.

## Notes

- The 2026 regulations and Red Bull season details were researched on 9 October 2026 and change quickly. Check the latest news before relying on them.
- Worked examples and the synthetic dataset use round, illustrative numbers, not real team data.
- This is an independent study resource. It is not affiliated with or endorsed by Red Bull Racing, Formula 1 or the FIA.
- Sources are listed at the end of the guide.
