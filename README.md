# Number Factorizer

A simple Python package to find **all factors** and **prime factorization** of any integer.

## Installation

```bash
pip install number-factorizer
```

Or install directly from GitHub:

```bash
pip install git+https://github.com/sohanananthula2012-ship-it/number-factorizer.git
```

## Usage

```python
from number_factorizer import get_factors, prime_factors, factorize

# Get all positive factors
print(get_factors(528))
# Output: [1, 2, 3, 4, 6, 8, 11, 12, 16, 22, 24, 33, 44, 48, 66, 88, 132, 176, 264, 528]

# Get prime factorization as dictionary
print(prime_factors(528))
# Output: {2: 4, 3: 1, 11: 1}

# Get nice string representation
print(factorize(528))
# Output: 2^4 × 3 × 11
```

## Features

- Find all positive factors of a number
- Get prime factorization
- Clean string output for prime factors
- Handles negative numbers (uses absolute value)
- Fast algorithm (checks only up to √n)

## License

MIT
