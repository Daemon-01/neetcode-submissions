class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        ways = [1] + [0] * amount

        for coin in coins:
            for idx in range(coin, amount+1):
                ways[idx] += ways[idx - coin]
        return ways[amount]