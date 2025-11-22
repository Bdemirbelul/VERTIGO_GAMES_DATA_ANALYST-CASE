from src.config import ABTestConfig
from src.simulation import (
    simulate_baseline,
    simulate_with_sale,
    simulate_with_new_source,
)
from src.plotting import plot_dau, plot_cumulative_revenue


def main():
    config = ABTestConfig()

    # Baseline
    df_base = simulate_baseline(config)
    plot_dau(df_base, "plots/dau_baseline.png")
    plot_cumulative_revenue(df_base, "plots/revenue_cumulative_baseline.png")

    # Sale scenario
    df_sale = simulate_with_sale(config)
    plot_cumulative_revenue(df_sale, "plots/revenue_cumulative_sale.png")

    # New source scenario
    df_new = simulate_with_new_source(config)
    plot_cumulative_revenue(df_new, "plots/revenue_cumulative_new_source.png")


if __name__ == "__main__":
    main()

