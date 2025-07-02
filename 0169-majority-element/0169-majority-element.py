class Solution(object):
    def majorityElement(self, nums):
        nums = sorted(nums)
        return (nums[len(nums) /2])
