class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}
        def dfs(remaining):
            if remaining == 0:
                return 1
            if remaining < 0 :
                return 0
            if remaining in memo:
                return memo[remaining]
            count = 0

            for num in nums:
                count += dfs(remaining - num)
            memo[remaining] = count
            return count

        return dfs(target)