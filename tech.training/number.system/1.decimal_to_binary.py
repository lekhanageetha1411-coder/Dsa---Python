
n = int(input("Enter a decimal to convert to binary:"))
output = " "

for i in range(1,11):
    output = str(n%2) +output
    n = n//2
print("the output is:",output)    