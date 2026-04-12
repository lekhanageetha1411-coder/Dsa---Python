x = int(input("Enter a number to check whether it is palindrome or not"))

s = str(x)

rev = s[::-1]

if s == rev:
    print("True, x is a palindrome")

else:
    print("False, x is not an palindrome")