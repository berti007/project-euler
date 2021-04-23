# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
# The sum of these multiples is 23.
# 
# Find the sum of all the multiples of 3 or 5 below 1000.
def compute():
    a = range(1,1000)

    mult = []

    for ele in a:
        if (ele % 3 == 0 or ele % 5 == 0):
            mult.append(ele)


    sum = 0
    for ele in mult:
        sum += ele

    return(sum)

if __name__ == "__main__":
	print(compute())