class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        balloons = [1] + nums + [1]
        memo = {}

        def burst(left: int, right: int) -> int:
            key = (left, right)

            if key in memo:
                return memo[key]

            # No balloons remain between these boundaries.
            if right - left <= 1:
                return 0

            best = 0

            # Choose k as the last balloon to burst in this interval.
            for k in range(left + 1, right):
                coins = (
                    balloons[left] * balloons[k] * balloons[right]
                    + burst(left, k)
                    + burst(k, right)
                )
                best = max(best, coins)

            memo[key] = best
            return best

        return burst(0, len(balloons) - 1)
