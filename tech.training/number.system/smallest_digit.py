n = int(input("ENter the number to find the smallest digit in it:"))
small_dig = n % 10

while n != 0:
    dig = n % 10
    if dig < small_dig:
        small_dig = dig
    n = n // 10
print(small_dig)    