class Solution(object):
    def maxProfit(self, prices):
        n = len(prices)
        left_profit = [0] * n
        min_profit = prices[0]
        
        # First pass: left to right (max profit if sold up to i)
        for i in range(1, n):
            min_profit = min(min_profit, prices[i])
            left_profit[i] = max(left_profit[i-1], prices[i] - min_profit)
        
        right_profit = [0] * n
        max_profit = prices[-1]
        
        # Second pass: right to left (max profit if bought from i)
        for i in reversed(range(n-1)):
            max_profit = max(max_profit, prices[i])
            right_profit[i] = max(right_profit[i+1], max_profit - prices[i])
        
        # Combine both
        max_total = 0
        for i in range(n):
            max_total = max(max_total, left_profit[i] + right_profit[i])
        
        return max_total

