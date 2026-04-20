n = 153
arm = n
sum =0

while(n != 0):
    last = n%10
    sum += last*last*last
    n= n//10
if(arm == sum):
    print("armstrong")
else:
    print("not an armstrong value:")
    