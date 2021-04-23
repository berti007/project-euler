# The sum of the squares of the first ten natural numbers is,

# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,

# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def compute():
    ran = range(1,101)

    sum1 = 0
    sum2 = 0

    for x in ran:
        sum1 += (x * x)
        sum2 += x

    return((sum2 * sum2) - sum1)

if __name__ == "__main__":
	print(compute())