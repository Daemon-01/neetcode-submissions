class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, cur = [], []
        used = set()

        def dfs():
            if len(cur) == len(nums):
                res.append(cur.copy())
                return
            
            for num in nums:
                if num not in cur:
                    cur.append(num); used.add(num)
                    dfs()
                    cur.pop(); used.remove(num)
        dfs()
        return res