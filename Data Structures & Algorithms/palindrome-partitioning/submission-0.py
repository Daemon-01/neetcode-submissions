class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, sol = [], []

        def dfs(idx):
            # Base Case 
            if idx == len(s):
                res.append(list(sol))
                return
            for i in range(idx, len(s)):
                subString = s[idx : i+1]
                if subString == subString[::-1]:
                    sol.append(subString)
                    dfs(i+1)
                    sol.pop()
        dfs(0)
        return res
