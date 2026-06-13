class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        for i in range(len(prices)):
            buy = prices[i]
            if i+1 < len(prices):
                sell = prices[i+1]
                if sell - buy > 0:
                    maxProfit += sell - buy
        return maxProfit