class Solution(object):
    def twoSum(self, nums, target):
        hashmap = {}
        for i in range(len(nums)):
            num = nums[i]
            com = target - nums[i]
            if com in hashmap:
                return (hashmap[com],i)
            hashmap[num] =i
        return []