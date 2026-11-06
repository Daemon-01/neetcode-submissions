class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def sumIndex(idx, sum):
            key = (idx, sum)
            if key in memo:
                return memo[key]
            if idx == len(nums):
                return 1 if sum == target else 0
            count = 0

            count += sumIndex(idx+1, sum+nums[idx])
            count += sumIndex(idx+1, sum-nums[idx])

            memo[key] = count
            return count
        return sumIndex(0, 0)