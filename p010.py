# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

import euler, numpy

def compute():
    n = 2000000
    return(numpy.sum(euler.SieveOfEratosthenes(n)))

if __name__ == "__main__":
    print(compute())