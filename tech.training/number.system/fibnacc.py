# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Try programiz.pro")
def fib(n):
     if n == 0:
         return 0
     if n == 1:
         return 1
     
     a = 0
     b = 1
     c = 0 
     for i in range(2,n+1):
         c = a+b
         a = b
         b = c
         
     return c
n = 10
print("fib of "+str(n)+" is:"+ str(fib(n)))
     