class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = 0
        for sell in range(len(prices)):
            curProfit = 0
            if prices[sell] > prices[buy]:
                curProfit = prices[sell] - prices[buy]
                profit = max(profit,curProfit)
            else:
                buy = sell
        return profit