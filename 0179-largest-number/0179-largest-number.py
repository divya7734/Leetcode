class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        n=len(nums)
        for i in range(n):
            if(nums[i]!=0):
                break
        else:
            return ("0")
        nums=list(map(str,nums))            
        for i in range(n):
            for j in range(i+1,n):
                if (int(nums[i]+nums[j])<int(nums[j]+nums[i])):
                    nums[i],nums[j]=nums[j],nums[i]
        return ("".join(nums))