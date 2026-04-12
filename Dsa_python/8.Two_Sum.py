nums = list(map(int,input("ENter the nums:").split()))
target = 9

for i in range(0,len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i] + nums[j] == target:
            print([i,j])