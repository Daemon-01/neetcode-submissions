class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)

        # Zero coins are needed to make amount 0
        dp[0] = 0

        for current_amount in range(1, amount + 1):
            for coin in coins:
                if coin <= current_amount:
                    dp[current_amount] = min(
                        dp[current_amount],
                        dp[current_amount - coin] + 1
                    )

        return -1 if dp[amount] == float("inf") else dp[amount]
