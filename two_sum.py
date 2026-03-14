#two sum problem
class Solution(object):
    def twoSum(self, nums, target):
        n=len(nums)
        hashmap={}
        
        for i in range (0,n) :
            rem=target-nums[i]
            if rem in hashmap:
                return [hashmap[rem],i]

            hashmap[nums[i]]=i

        