import math
from typing import Callable, List, Tuple

RetentionFn = Callable[[int], float]


def make_piecewise_exponential(points: List[Tuple[int, float]]) -> RetentionFn:
     """
    Eldeki retention noktalarından (D1, D3, D7, D14) düzgün bir eğri çıkarıyoruz.
    Kısaca: "arada ne oluyor?" sorusunu kendimiz exponent'la dolduruyoruz.
    """ 
    points = sorted(points, key=lambda x: x[0])
    segments = []

    for (d1, r1), (d2, r2) in zip(points, points[1:]):
        k = -(1.0 / (d2 - d1)) * math.log(r2 / r1)
        segments.append((d1, d2, r1, k))

    last_day, last_ret = points[-1]
    last_k = segments[-1][3]

    def retention(age: int) -> float:
        if age <= 0:
            return 1.0  # install day
        for d1, d2, r1, k in segments:
            if d1 <= age <= d2:
                return r1 * math.exp(-k * (age - d1))
        # beyond last point: extend the last segment
        return last_ret * math.exp(-last_k * (age - last_day))

    return retention


_points_A_old = [(1, 0.53), (3, 0.27), (7, 0.17), (14, 0.06)]
_points_B_old = [(1, 0.48), (3, 0.25), (7, 0.19), (14, 0.09)]

retention_A_old: RetentionFn = make_piecewise_exponential(_points_A_old)
retention_B_old: RetentionFn = make_piecewise_exponential(_points_B_old)


def retention_A_new(age: int) -> float:
    if age <= 0:
        return 1.0
    return 0.58 * math.exp(-0.12 * (age - 1))


def retention_B_new(age: int) -> float:
    if age <= 0:
        return 1.0
    return 0.52 * math.exp(-0.10 * (age - 1))

