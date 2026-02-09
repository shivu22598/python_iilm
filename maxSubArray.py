def maxSubArray(nums):
    maxValue=nums[0]
    sum=0
    for v in nums:
        sum+=v
        maxValue=max(maxValue,sum)
        if sum<0:
            sum=0
    return maxValue
nums=[5,4,-1,7,8]
print(maxSubArray(nums))    
    
    