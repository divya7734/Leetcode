class Solution(object):
    def maximumDifference(self, nums):
        min_num ,max_diff = nums[0], -1
        for i in nums:
            if i> min_num:
                max_diff = max(max_diff,i-min_num)
            else:
                min_num = i
        return max_diff