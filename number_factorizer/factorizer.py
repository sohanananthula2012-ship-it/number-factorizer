def get_factors(n: int) -> list[int]:
    """
    Returns all positive factors of n in ascending order.
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n == 0:
        raise ValueError("Cannot find factors of 0")
    
    n = abs(n)
    factors = set()
    
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            factors.add(i)
            factors.add(n // i)
    
    return sorted(factors)


def prime_factors(n: int) -> dict[int, int]:
    """
    Returns prime factorization as a dictionary {prime: exponent}
    Example: 528 → {2: 4, 3: 1, 11: 1}
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n == 0:
        raise ValueError("Cannot factorize 0")
    
    n = abs(n)
    factors = {}
    
    # Check for number of 2s
    while n % 2 == 0:
        factors[2] = factors.get(2, 0) + 1
        n //= 2
    
    # Check odd factors
    i = 3
    while i * i <= n:
        while n % i == 0:
            factors[i] = factors.get(i, 0) + 1
            n //= i
        i += 2
    
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    
    return factors


def factorize(n: int) -> str:
    """
    Returns a nice string representation of prime factorization.
    Example: 528 → "2^4 × 3 × 11"
    """
    factors = prime_factors(n)
    parts = []
    
    for prime, exp in factors.items():
        if exp == 1:
            parts.append(str(prime))
        else:
            parts.append(f"{prime}^{exp}")
    
    return " × ".join(parts)
