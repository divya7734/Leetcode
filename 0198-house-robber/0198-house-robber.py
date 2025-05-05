class Solution:
    def rob(self, nums: List[int]) -> int:
        rob, norob = 0, 0
        for num in nums:
            newRob = norob + num
            newNoRob = max(norob, rob)
            rob, norob = newRob, newNoRob
        return max(rob, norob)   