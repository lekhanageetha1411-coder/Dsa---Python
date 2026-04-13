'''num = list(map(int,input("Enter the nums of Array:").split()))

temp = []

for i in range(len(num)):
    if num[i] != 0:
        temp.append(num[i])

zero = len(num) - len(temp)
for i in range(zero):
    temp.append(0)

print(temp)'''

'''num = list(map(int,input("Enter the nums pf arrays:").split()))

pos = 0
for i in range(len(num)):
    if num[i] != 0:
        num[pos] = num[i]
        pos +=1

for i in range(pos,len(num)):
    num[i] = 0

print(num[i])    '''

class Solution(object):
    def moveZeroes(self, nums):
        pos = 0
        nums = [0,1,2,0,1,0]

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[pos] = nums[i]
                pos += 1
        for i in range(pos,len(nums)):
            nums[i] = 0