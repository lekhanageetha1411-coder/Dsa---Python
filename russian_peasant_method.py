a = 10
b = 20 
res = 0
while(a>0):
    if(a&1)==1:
        res += b
    a>>=1
    b<<=1
print(res)    
