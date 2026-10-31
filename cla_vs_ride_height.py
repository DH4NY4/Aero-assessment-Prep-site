"""C_L·A against ride height, with 95% confidence intervals.

Project 1 from the revision guide (Part 11 / Part 15). If runs.csv is not
present, a synthetic dataset is generated so the script runs out of the box.
The synthetic numbers are illustrative only, not real team data.

Usage:
    python scripts/cla_vs_ride_height.py            # uses or creates runs.csv
    python scripts/cla_vs_ride_height.py my.csv     # your own data

Expected columns: speed_ms, rho, ride_mm, downforce_N
"""
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def make_synthetic(path: Path, seed: int = 0) -> None:
    rng = np.random.default_rng(seed)
    rows = []
    for ride in range(10, 51, 5):  # mm
        # Ground-effect curve: rises as the floor nears the ground, then chokes.
        cla_true = 4.0 + 1.2 * np.exp(-((ride - 22) / 12) ** 2) - 0.6 * np.exp(-((ride - 10) / 4) ** 2)
        for _ in range(8):
            v = rng.uniform(55, 80)        # m/s
            rho = rng.normal(1.20, 0.01)   # kg/m^3
            q = 0.5 * rho * v**2
            rows.append({
                "speed_ms": v,
                "rho": rho,
                "ride_mm": ride,
                "downforce_N": cla_true * q * rng.normal(1.0, 0.02),
            })
    pd.DataFrame(rows).to_csv(path, index=False)
    print(f"Created synthetic data: {path}")


def main() -> None:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("runs.csv")
    if not path.exists():
        make_synthetic(path)

    df = pd.read_csv(path)
    df["q"] = 0.5 * df["rho"] * df["speed_ms"] ** 2
    df["CLA"] = df["downforce_N"] / df["q"]  # m^2, downforce taken as positive

    g = df.groupby("ride_mm")["CLA"].agg(["mean", "std", "count"])
    g["ci95"] = 1.96 * g["std"] / np.sqrt(g["count"])
    print(g.round(3))

    plt.errorbar(g.index, g["mean"], yerr=g["ci95"], marker="o", capsize=3)
    plt.xlabel("Ride height (mm)")
    plt.ylabel("C_L·A (m²)")
    plt.title("C_L·A vs ride height (95% CI)")
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig("cla_vs_ride_height.png", dpi=150)
    print("Saved plot: cla_vs_ride_height.png")
    plt.show()


if __name__ == "__main__":
    main()
