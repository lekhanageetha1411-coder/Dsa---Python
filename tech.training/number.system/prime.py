n = 83
flag = True

for i in range(2,int(n**(0.5)+1)):
    if n % i == 0:
        flag = False
        break
if(flag == True):
    print("prime number")
else:
    print("not a prime")
    