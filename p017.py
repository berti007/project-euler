# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


# Note: Do not count spaces or hyphens. For example, 
# 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when 
# writing out numbers is in compliance with British usage.

def compute(n):
    ans = 0
    for i in range(1,n+1):
        ans = ans + len(toEnglish(i))
    
    return ans
    
ONES = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
        "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
TENS = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

def toEnglish(n):
	if 0 <= n < 20:
		return ONES[n]
	elif 20 <= n < 100:
		return TENS[n // 10] + (ONES[n % 10] if (n % 10 != 0) else "")
	elif 100 <= n < 1000:
		return ONES[n // 100] + "hundred" + (("and" + toEnglish(n % 100)) if (n % 100 != 0) else "")
	elif 1000 <= n < 1000000:
		return toEnglish(n // 1000) + "thousand" + (toEnglish(n % 1000) if (n % 1000 != 0) else "")
	else:
		raise ValueError()

if __name__ == "__main__":
    print(compute(1000))