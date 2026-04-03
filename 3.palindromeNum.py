Class Solution(Object):
   def palNum(self, n):

     s = str(x)

     rev = s[::-1]
     if s == rev:
       return True

     else:
       return False

to run

x = int(input("Enter number:"))
s = str(x)

rev = s[::-1]
if s == rev:
  print("True")

else:
  print("False")
  
