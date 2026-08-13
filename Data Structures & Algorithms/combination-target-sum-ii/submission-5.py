class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(idx, cur, sum):
            # base cases
            if sum == target:
                res.append(list(cur))
                return
            
            if sum > target or idx == len(candidates):
                return
            
            # include the current element
            cur.append(candidates[idx])
            dfs(idx + 1, cur, sum + candidates[idx])

            # exclude the current element
            cur.pop()
            while idx + 1 < len(candidates) and candidates[idx] == candidates[idx + 1]:
                idx += 1
            dfs(idx + 1, cur, sum)
        dfs(0, [], 0)
        return res