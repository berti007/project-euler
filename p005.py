# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import euler

def compute():
    ans = 1

    for i in range(1,21):
        ans = euler.kgv(ans,i)

    return ans

if __name__ == "__main__":
	print(compute())