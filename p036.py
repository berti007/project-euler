import euler

def compute():
    sum = 0
    for i in range(1,1000000):
        bi = str(bin(i))[2:]
        if euler.palindrom_check(i) & euler.palindrom_check(bi):
            sum = sum + i
    return sum

if __name__ == "__main__":
    print(compute())