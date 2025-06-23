class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        d={}
        count = 0
        for num in time:
            rem = num % 60
            if ((60-rem)%60 in d ):
                count +=d[(60-rem) %60]
            if rem in d:
                d[rem]+=1
            else:
                d[rem]=1
        return count

        # for i in range(len(time)):
        #     if(time[i]+time[j]%60 ==0)
             