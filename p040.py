def compute():
    a = ""
    i = 1
    while len(a)<1000001:
        a = a + str(i)
        i += 1
    res = int(a[0]) * int(a[99]) * int(a[999]) * int(a[9999]) * int(a[99999]) * int(a[999999]) 
    return res

if __name__ == "__main__":
    print(compute())