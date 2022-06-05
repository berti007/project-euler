def compute():
    ans = sum(pow(i, i, 10**10) for i in range(1, 1001)) % (10**10)
    return ans

if __name__ == "__main__":
    print(compute())