class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        def dfs(idx, curr):
            if idx == len(nums):
                res.append(curr)
                return
            #includes the current element
            dfs(idx+1, curr+[nums[idx]])
            # excludes the current element
            dfs(idx+1, curr)
        dfs(0, curr)
        return res