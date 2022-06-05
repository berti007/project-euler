import euler

def compute():
    m = 0
    p = 0
    for a in range(-1000,1000):
        for b in range(-1000,1000):
            n = 0
            while(euler.is_prime(n*n+a*n+b)):
                if n > m:
                    m = n
                    p = a * b
                n = n+1
    return p

if __name__ == "__main__":
    print(compute())