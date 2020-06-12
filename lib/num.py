"""Helper functions for number operations"""

import math


def co_prime_num(num):
    """Naive way to calculates amount of co-prime numbers"""

    co_primes = [c for c in range(num) if math.gcd(num, c) == 1]

    return len(co_primes)

def gen_primes(num):
    """Using Sieve Eratosthenes"""

    primes_acc = [True] * num
    primes_acc[0] = False
    primes_acc[1] = False

    for i, is_prime in enumerate(primes_acc):
        if is_prime:
            yield i
            for n in range(i**2, num, i):
                primes_acc[n] = False
