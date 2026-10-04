class Solution:
    def numSquares(self, n: int) -> int:
        squares = [i * i for i in range(1, int(math.sqrt(n)) + 1)]
        dp = [0] + [float("inf")] * n

        for i in range(1, n+1):
            for square in squares:
                if square > i:
                    break
                dp[i] = min(dp[i], dp[i-square] + 1)
        return dp[n]