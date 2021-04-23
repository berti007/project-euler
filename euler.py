import math

def divisors(n):
    return [d for d in range(2,n//2+1) if n % d == 0 ]
# Returns the prime numbers of n
def primes(n):
    return [ d for d in divisors(n) if \
             all( d % od != 0 for od in divisors(n) if od != d ) ]

# Returns groesste gemeinsame Teiler for a and b
def ggt(a, b):
    while b != 0:
        c = a % b
        a, b = b, c
    return a

# Returns kleinstes gemeinsames Vielfaches for a and b
def kgv(a, b):
    return (a * b) / ggt(a, b) 


def SieveOfEratosthenes(n): 
      
    # Create a boolean array "prime[0..n]" and initialize 
    # all entries it as true. A value in prime[i] will 
    # finally be false if i is Not a prime, else true. 
    prime = [True for i in range(n + 1)] 
    p = 2
    while (p * p <= n): 
          
        # If prime[p] is not changed, then it is a prime 
        if (prime[p] == True): 
              
            # Update all multiples of p 
            for i in range(p * 2, n + 1, p): 
                prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False


    # Print all prime numbers 
    return [p for p in range(n + 1) if prime[p]]

def binomial(n, k):
	assert 0 <= k <= n
	return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

def quersumme(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s