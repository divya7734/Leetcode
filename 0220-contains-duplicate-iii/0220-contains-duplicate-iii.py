from sortedcontainers import SortedList

class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        if valueDiff < 0 or indexDiff < 0:
            return False

        window = SortedList()

        for i in range(len(nums)):
            num = nums[i]

            # Find the smallest number >= num - valueDiff
            pos = window.bisect_left(num - valueDiff)

            # Check if this candidate is within valueDiff range
            if pos < len(window) and abs(window[pos] - num) <= valueDiff:
                return True

            # Add current number to window
            window.add(num)

            # Keep the window size ≤ indexDiff
            if i >= indexDiff:
                window.remove(nums[i - indexDiff])

        return False
