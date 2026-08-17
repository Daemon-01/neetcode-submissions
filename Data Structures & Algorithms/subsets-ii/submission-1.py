class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res, cur = [], []
        # used = set()

        def dfs(idx):
            if idx == len(nums):
                res.append(list(cur))
                return
            # choose the current element
            cur.append(nums[idx])
            dfs(idx+1)

            # exclude the current element
            cur.pop()
            while idx+1 < len(nums) and nums[idx] == nums[idx+1]:
                idx += 1
            dfs(idx+1)
        dfs(0)
        return res