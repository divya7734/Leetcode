class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefix_count = {0: 1}  # Base case: one subarray with sum 0
        curr_sum = 0
        count = 0

        for num in nums:
            curr_sum += num

            # Check if (curr_sum - k) has occurred before
            if (curr_sum - k) in prefix_count:
                count += prefix_count[curr_sum - k]

            # Update prefix_count with current curr_sum
            if curr_sum in prefix_count:
                prefix_count[curr_sum] += 1
            else:
                prefix_count[curr_sum] = 1

        return count
