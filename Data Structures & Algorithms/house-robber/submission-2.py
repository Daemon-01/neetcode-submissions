class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [0] * (n+1)
        dp[0], dp[1] = 0, nums[0]

        for i in range(2, n+1):
            skip = dp[i-1]
            rob = dp[i-2] + nums[i-1]

            dp[i] = max(skip, rob)
        return dp[n]