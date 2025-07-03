class Solution(object):
    def maxProfit(self, prices):
        min_n = prices[0]
        max_profit = 0
        for i in prices:
            if i< min_n:
                min_n = i
            else:
                profit = i - min_n
                if profit > max_profit:
                    max_profit = profit
        return max_profit