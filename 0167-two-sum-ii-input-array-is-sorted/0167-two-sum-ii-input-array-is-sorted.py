class Solution(object):
    def twoSum(self, numbers, target):
        l ,r = 0, len(numbers)-1
        while l<r:
            total = numbers[l] + numbers[r]
            if total == target :
                return (l+1 , r+1)
            elif total < target :
                l+=1
            else:
                r-=1
        return []
        