class Solution(object):
    def minimumOperations(self, nums):
        return (len(set(nums)- {0}))
        