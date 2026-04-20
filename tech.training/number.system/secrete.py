# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Try programiz.pro")
n = 10
a = 0
b = 1
for i in range(2,n+1):
    c = (i -1)*(a+b)
    a = b
    b = c
print(c)