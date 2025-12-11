# Binomial Trees Option Pricer

Minimal Python function to price vanilla European or American calls/puts with a Cox–Ross–Rubinstein binomial tree.

## Function
- `price_binomial_option(option="call", exercise="european", strike=1.0, spot=1.0, vol=0.2, rfr=0.0, texp=1.0, steps=100)`  
  Returns `(price, elapsed_seconds, num_paths)`.
  - `option`: `"call"` or `"put"`
  - `exercise`: `"european"` or `"american"`
  - `strike`: strike price
  - `spot`: current underlying price
  - `vol`: volatility (annualized)
  - `rfr`: risk-free rate (continuously compounded)
  - `texp`: time to expiry in years
  - `steps`: number of binomial steps

## Usage
```python
from option_pricing import price_binomial_option

price, elapsed, paths = price_binomial_option(
    option="call",
    exercise="american",
    strike=100,
    spot=105,
    vol=0.2,
    rfr=0.03,
    texp=1.0,
    steps=200,
)
print(price, elapsed, paths)
```
