class solution(object):
  def runnigSum(self,nums):

    for i in range(1, len(nums)):
      nums[i] = nums[i] + nums[i - 1]
    return nums
    # the code has to be write in leetcode to run it we have to use the below code

nums = [1,2,3,3]

for i in range(1, len(nums)):
  nums[i] = nums[i] + nums[i - 1]

print(nums)
