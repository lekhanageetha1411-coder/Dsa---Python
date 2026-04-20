print("Try programiz.pro")
num = int(input("ENter the numbers to find bin digits:"))
for i in range(1, num+1):   # loop from 1 to 10
    output = ""          # reset output for each number
    n = i            # copy of n for division
    
    while n > 0:
        output = str(n % 2) + output
        n = n // 2
    
    print(f"{i} in binary is: {output}")
