num = [1,2,3,3]
duplicate = False
for i in range(len(num)):
    for j in range(i+1,(len(num))):
        if num[i] == num[j]:
            duplicate = True

if duplicate:
    print(True)
else:
    print(False)    