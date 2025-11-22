from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def plot_dau(df: pd.DataFrame, outfile: str) -> None:
    Path(outfile).parent.mkdir(parents=True, exist_ok=True)
    



 #A/b grafiği hangisi güçlü görmek adına 
    plt.figure()
    plt.plot(df["day"], df["dau_A"], label="DAU - Variant A")
    plt.plot(df["day"], df["dau_B"], label="DAU - Variant B")
    plt.xlabel("Day")
    plt.ylabel("Daily Active Users")
    plt.title("DAU over Time")
    plt.legend()
    plt.tight_layout()
    plt.savefig(outfile)
    plt.close()


def plot_cumulative_revenue(df: pd.DataFrame, outfile: str) -> None:
    Path(outfile).parent.mkdir(parents=True, exist_ok=True)

    cum_A = df["rev_A"].cumsum()
    cum_B = df["rev_B"].cumsum()

    plt.figure()
    plt.plot(df["day"], cum_A, label="Cumulative Revenue - A")
    plt.plot(df["day"], cum_B, label="Cumulative Revenue - B")
    plt.xlabel("Day")
    plt.ylabel("Cumulative Revenue")
    plt.title("Cumulative Revenue over Time")
    plt.legend()
    plt.tight_layout()
    plt.savefig(outfile)
    plt.close()

