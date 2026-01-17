def twosum(nums, target):
    n=len(nums)
    for i in range(n):
        for j in range(i+1,n):
            if nums[i]+nums[j]==target:
                return [i,j]
    return []
nums=[12,7,8,13,9]
target=17
result=twosum(nums,target)
print("Indices of the two numbers that add up to", target, "are:", result)
   