class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        set1 = set()
        for i in range(len(nums)):
            if nums[i] in set1 :
                return True
            set1.add(nums[i])
            if len(set1) > k:
                set1.remove(nums[i-k])
        return False