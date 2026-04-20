
div = 7
rem = 0


for i in range(len(n)):
    rem = (rem * 10 + int(n[i]))%div
if rem == 0:
    print("divisible")
else:
    print("not divisible")