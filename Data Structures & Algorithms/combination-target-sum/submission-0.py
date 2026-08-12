class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, curr = [], []
        # define the recursive function
        def dfs(idx, sum):
            # if sum equal to target return
            if sum == target:
                    res.append(list(curr))
                    return
            # base case of recursive function and earling pruning
            if sum > target or idx == len(nums):
                return
            # include the current element in the sum
            curr.append(nums[idx])
            dfs(idx, sum+nums[idx])

            #exclude the current element in the sum
            curr.pop()
            dfs(idx+1, sum)
        dfs(0, 0)
        return res