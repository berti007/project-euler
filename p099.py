def compute():
    with open('p099_base_exp.txt') as f:
        lines = f.readlines()
    counter = 1
    m = 1
    prod = 0
    for line in lines:
        currentline = line.split(",")
        if int(currentline[0])**int(currentline[1]) > prod:
            m = counter
            prod = int(currentline[0])**int(currentline[1])
        counter = counter + 1
        print(counter)
    return m

if __name__ == "__main__":
    print(compute())
    
# Solution : 709