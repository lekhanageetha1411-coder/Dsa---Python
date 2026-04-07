class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        if sorted(s) == sorted(t):
            return True
        else:
            return False            or


s = input("enter the word:")
t = input("Enter the 2nd word:")

if(len(s)) != len(t):
    print(False)

if sorted(s)  ==sorted(t):
    print(True)

else:
    print(False)    
