class Solution(object):
    def maxProfit(self, prices):
        n = len(prices)
        left_profit = [0]*n
        min_profit = prices[0]
        for i in range(1, n):
            min_profit = min(prices[i],min_profit)
            left_profit[i]= max(left_profit[i-1],prices[i]-min_profit)
        right_profit =[0]*n
        max_profit = prices[-1]
        for i in reversed(range(n-1)):
            max_profit = max(max_profit,prices[i])
            right_profit[i] = max(right_profit[i+1],max_profit - prices[i])
        max_total =0
        for i in range(n):
            max_total = max(max_total, left_profit[i]+ right_profit[i])
        return max_total