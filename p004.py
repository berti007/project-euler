# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

def compute():
    ran = range(999,100,-1)
    number = 0;

    for x in ran:
        for y in ran:
            prod = x * y
            if prod == int(str(prod)[::-1]):
                if(prod > number):
                    number = prod

    return(number)

if __name__ == "__main__":
	print(compute())