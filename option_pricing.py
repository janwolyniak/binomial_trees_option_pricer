from math import exp, sqrt
from time import perf_counter


def price_binomial_option(
    option="call",
    exercise="european",
    strike=1.0,
    spot=1.0,
    vol=0.2,
    rfr=0.0,
    texp=1.0,
    steps=100,
):
    start = perf_counter()

    dt = texp / steps
    u = exp(vol * sqrt(dt))
    d = 1 / u
    disc = exp(-rfr * dt)
    p = (exp(rfr * dt) - d) / (u - d)

    prices = [spot * (u ** j) * (d ** (steps - j)) for j in range(steps + 1)]
    values = [
        max(pr - strike, 0.0) if option == "call" else max(strike - pr, 0.0)
        for pr in prices
    ]

    american = exercise == "american"
    for step in range(steps - 1, -1, -1):
        for i in range(step + 1):
            cont = disc * (p * values[i + 1] + (1 - p) * values[i])
            if american:
                spot_here = spot * (u ** i) * (d ** (step - i))
                exer = (
                    max(spot_here - strike, 0.0)
                    if option == "call"
                    else max(strike - spot_here, 0.0)
                )
                values[i] = max(cont, exer)
            else:
                values[i] = cont

    elapsed = perf_counter() - start
    num_paths = 2 ** steps
    return values[0], elapsed, num_paths


__all__ = ["price_binomial_option"]
