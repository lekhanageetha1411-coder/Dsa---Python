num = [1,2,3]

ans = []

for i in num:
    ans.append(i)
for i in num:
    ans.append(i)    
print(ans)    

or

class Solution(object):
    def getConcatenation(self, nums):
        ans  = []

        for i in nums:
            ans.append(i)
        for i in nums:
            ans.append(i)

        return ans
