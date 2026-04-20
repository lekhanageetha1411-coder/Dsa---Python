n= int(input("ENter a number:"))

sum_digits = 0

while n != 0:
    dig = n % 10
    sum_digits += dig
    n = n // 10
print(sum_digits)    