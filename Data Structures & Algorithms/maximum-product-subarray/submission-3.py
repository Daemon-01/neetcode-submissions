class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)

        max_dp = [0] * n
        min_dp = [0] * n

        max_dp[0] = nums[0]
        min_dp[0] = nums[0]
        result = nums[0]

        for i in range(1, n):
            num = nums[i]

            max_dp[i] = max(
                num,
                max_dp[i - 1] * num,
                min_dp[i - 1] * num
            )

            min_dp[i] = min(
                num,
                max_dp[i - 1] * num,
                min_dp[i - 1] * num
            )

            result = max(result, max_dp[i])

        return result
