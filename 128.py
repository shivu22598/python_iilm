class Solution(object):
    def longestConsecutive(self, nums):
        n=set(nums)
        res=0
        for i in n:
             if i-1 not in n:
                j=i+1
                while j in n:
                    j+=1
                res=max(res,j-i)
        return res 