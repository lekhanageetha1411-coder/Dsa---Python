n = int(input("Enter the number :"))

prod_odd = 1
has_odd = False

while n!=0:
    dig = n % 10
    if(dig % 2) != 0:
        prod_odd *= dig
        has_odd = True
    n = n // 10 
if has_odd:
    print("it has a odd digits:"+prod_odd)        
else:
    print("no odd digit")