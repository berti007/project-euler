import math

def compute():
    sum = 0
    for i in range(3,1000000):
        fac = 0
        stri = str(i)
        for l in range(0,len(stri)):
            fac = fac + math.factorial(int(stri[l]))
        if i == fac:
            sum += i
    return sum

if __name__ == "__main__":
    print(compute())