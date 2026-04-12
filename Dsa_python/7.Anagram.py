s = input("enter the word:")
t = input("Enter the 2nd word:")

if(len(s)) != len(t):
    print(False)

if sorted(s)  ==sorted(t):
    print(True)

else:
    print(False)    