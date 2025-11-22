from dataclasses import asdict
from typing import Optional

import pandas as pd

from src.config import ABTestConfig
from src.retention import (
    retention_A_old,
    retention_B_old,
    retention_A_new,
    retention_B_new,
)

    # Günün parasını hesapladığımız yer. DAU * satın alma + reklam geliri.

def _compute_daily_revenue(
    dau: float,
    purchase_rate: float,
    ecpM: float,
    imps_per_dau: float,
) -> dict:
    rev_iap = dau * purchase_rate
    rev_ads = dau * imps_per_dau * ecpM / 1000.0
    return {
        "rev_total": rev_iap + rev_ads,
        "rev_iap": rev_iap,
        "rev_ads": rev_ads,
    }

def simulate_baseline(config: Optional[ABTestConfig] = None) -> pd.DataFrame:
  # En basic senaryo: klasik 20k install akıyor, sale yok, yeni kaynak yok.
    if config is None:
        config = ABTestConfig()

    rows = []
    for day in range(1, config.days + 1):
        dau_A = 0.0
        dau_B = 0.0

        for cohort_day in range(1, day + 1):
            age = day - cohort_day
            installs = config.installs_per_day
            dau_A += installs * retention_A_old(age)
            dau_B += installs * retention_B_old(age)
    # Her iki varyantın bugün kasaya bıraktığı para

        revA = _compute_daily_revenue(
            dau_A,
            config.purchase_rate_A,
            config.eCPM_A,
            config.imps_per_dau_A,
        )
        revB = _compute_daily_revenue(
            dau_B,
            config.purchase_rate_B,
            config.eCPM_B,
            config.imps_per_dau_B,
        )

        rows.append(
            {
                "day": day,
                "dau_A": dau_A,
                "dau_B": dau_B,
                "rev_A": revA["rev_total"],
                "rev_B": revB["rev_total"],
                "rev_A_iap": revA["rev_iap"],
                "rev_B_iap": revB["rev_iap"],
                "rev_A_ads": revA["rev_ads"],
                "rev_B_ads": revB["rev_ads"],
            }
        )

    return pd.DataFrame(rows)

#15. günden itibaren 10 gün SALE var , alışveriş oranı 1% artıyor.
def simulate_with_sale(
    config: Optional[ABTestConfig] = None,
    sale_start: int = 15,
    sale_length: int = 10,
    sale_lift_abs: float = 0.01,
) -> pd.DataFrame:
   
    if config is None:
        config = ABTestConfig()

    sale_end = sale_start + sale_length - 1
    rows = []

    for day in range(1, config.days + 1):
        dau_A = dau_B = 0.0

        for cohort_day in range(1, day + 1):
            age = day - cohort_day
            installs = config.installs_per_day
            dau_A += installs * retention_A_old(age)
            dau_B += installs * retention_B_old(age)

        purchase_A = config.purchase_rate_A
        purchase_B = config.purchase_rate_B
        if sale_start <= day <= sale_end:
            purchase_A += sale_lift_abs
            purchase_B += sale_lift_abs

        revA = _compute_daily_revenue(
            dau_A, purchase_A, config.eCPM_A, config.imps_per_dau_A
        )
        revB = _compute_daily_revenue(
            dau_B, purchase_B, config.eCPM_B, config.imps_per_dau_B
        )

        rows.append(
            {
                "day": day,
                "dau_A": dau_A,
                "dau_B": dau_B,
                "rev_A": revA["rev_total"],
                "rev_B": revB["rev_total"],
                "rev_A_iap": revA["rev_iap"],
                "rev_B_iap": revB["rev_iap"],
                "rev_A_ads": revA["rev_ads"],
                "rev_B_ads": revB["rev_ads"],
            }
        )

    return pd.DataFrame(rows)


def simulate_with_new_source(
    config: Optional[ABTestConfig] = None,
    new_source_start: int = 20,
    old_installs_per_day_after: int = 12_000,
    new_installs_per_day: int = 8_000,
) -> pd.DataFrame:
  
    if config is None:
        config = ABTestConfig()

    rows = []

    for day in range(1, config.days + 1):
        dau_A = dau_B = 0.0

        for cohort_day in range(1, day + 1):
            age = day - cohort_day

            if cohort_day < new_source_start:
      
                old_installs = config.installs_per_day
                new_installs = 0
            else:
                old_installs = old_installs_per_day_after
                new_installs = new_installs_per_day

            dau_A += old_installs * retention_A_old(age) + new_installs * retention_A_new(age)
            dau_B += old_installs * retention_B_old(age) + new_installs * retention_B_new(age)

        revA = _compute_daily_revenue(
            dau_A, config.purchase_rate_A, config.eCPM_A, config.imps_per_dau_A
        )
        revB = _compute_daily_revenue(
            dau_B, config.purchase_rate_B, config.eCPM_B, config.imps_per_dau_B
        )

        rows.append(
            {
                "day": day,
                "dau_A": dau_A,
                "dau_B": dau_B,
                "rev_A": revA["rev_total"],
                "rev_B": revB["rev_total"],
                "rev_A_iap": revA["rev_iap"],
                "rev_B_iap": revB["rev_iap"],
                "rev_A_ads": revA["rev_ads"],
                "rev_B_ads": revB["rev_ads"],
            }
        )

    return pd.DataFrame(rows)
