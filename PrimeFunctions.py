import math
import numpy as np
import mpmath
import random
import concurrent.futures

# Function to check if a number is prime using the Miller-Rabin test

def miller_rabin_round(args):
    n, s, r = args
    a = random.randrange(2, n - 1)
    x = pow(a, s, n)
    if x == 1 or x == n - 1:
        return True
    for _ in range(r - 1):
        x = pow(x, 2, n)
        if x == n - 1:
            return True
    return False

def is_prime(n, k=20):
    """
    Determines if n is a prime number using the Miller-Rabin primality test.

    Args:
        n (int): The number to test for primality.
        k (int): The number of rounds (iterations) to perform. Higher k increases accuracy.

    Returns:
        bool: True if n is probably prime, False if n is composite.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2

    args = [(n, s, r)] * k
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = list(executor.map(miller_rabin_round, args))
    return all(results)

# Function to find the largest prime factor of a number
def largest_prime_factor(n):
    if n <= 1:
        return None
    max_prime = -1

    # Remove factors of 2
    while n % 2 == 0:
        max_prime = 2
        n //= 2

    # Try dividing by odd numbers up to sqrt(n)
    i = 3
    sqrt_n = math.isqrt(n)
    while i <= sqrt_n and n > 1:
        if n % i == 0:
            max_prime = i
            while n % i == 0:
                n //= i
            sqrt_n = math.isqrt(n)
        i += 2

    # If n is a prime number greater than 2
    if n > 2:
        max_prime = n

    return max_prime
