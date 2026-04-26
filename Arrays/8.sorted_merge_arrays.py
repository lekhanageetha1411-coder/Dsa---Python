num1 =  [1,2,3,0,0,0]
num2 =  [2,5,6]

m = len([x for x in num1 if x != 0])
n = len(num2)

j = m - 1
i = n - 1
k = m + n -1

while i >=0 and j >= 0:
    if i>= 0 and num1[i] > num2[j]:
        num1[k] = num1[i]
        i -= 1
    else:
        num1[k] = num2[j]
        j -= 1

    k -= 1
while j >= 0:
    num1[k] = num2[j]
    j -=1
    k-=1
print(num1)