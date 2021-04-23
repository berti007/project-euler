# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

import euler

def compute():
    n = 100000
    while len(euler.SieveOfEratosthenes(n)) < 10001:
        n *= 10
    return euler.SieveOfEratosthenes(n)[10000]


if __name__ == "__main__":
	print(compute())