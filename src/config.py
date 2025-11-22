from dataclasses import dataclass


#aldığım matrixdeki veriler buraya dataclass olarak girildi 

@dataclass
class ABTestConfig:
    days: int = 30
    installs_per_day: int = 20_000

    # Metriks daily purchase ratio verileri
    purchase_rate_A: float = 0.0305
    purchase_rate_B: float = 0.0315

    # ecpm  verileri
    eCPM_A: float = 9.8
    eCPM_B: float = 10.8
    # Ad monetization verileri

    imps_per_dau_A: float = 2.3
    imps_per_dau_B: float = 1.6

