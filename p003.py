# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

import euler

# print(primes(num))
def compute(num: int):
    newnumm = num
    largestFact = 0;
    
    counter = 2;
    while (counter * counter <= newnumm):
        if (newnumm % counter == 0):
            newnumm = newnumm / counter;
            largestFact = counter;
        else:
            counter += 1;
        

    if (newnumm > largestFact):
        largestFact = newnumm

    return(largestFact)

if __name__ == "__main__":
	print(compute(600851475143))