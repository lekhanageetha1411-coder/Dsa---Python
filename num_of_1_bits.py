class Solution(object):
    def hammingWeight(self, n):
        ones = 0
        count = 0
        while(n != 0):
            ones += (n&1)
            n>>=1
            count = count +1
        return ones        
        
