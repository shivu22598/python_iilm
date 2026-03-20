class Solution(object):
    def subarraySum(self, nums, k):
        sum = 0
        count = 0
        hashmap ={0:1}
        for num in nums:
            sum += num
            if sum - k in hashmap:
                count += hashmap[sum-k]
            hashmap[sum] = hashmap.get(sum,0)+1
        return count
      