import math

def compute():
    counter = 0
    for n in range(1,101):
        for r in range(1,n):
            bio = math.factorial(n)/(math.factorial(r)*math.factorial(n-r))
            if bio > 1000000:
                # print(n, " over ", r, " is equals ", bio)
                counter = counter + 1
    return counter

if __name__ == "__main__":
    print(compute())