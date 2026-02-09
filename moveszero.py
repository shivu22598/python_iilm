def moveZeroes(nums):
    l=len(nums)
    i=0
    for j in range(l):
        if nums[j]!=0:
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
    return nums
nums=[1,0,3,0,12]
print(moveZeroes(nums))