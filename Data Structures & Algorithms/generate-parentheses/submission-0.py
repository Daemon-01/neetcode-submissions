class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans, sol = [], []

        def dfs(openN, closeN):
            if openN == closeN == n:
                ans.append("".join(sol))

            if openN < n:
                sol.append("(")
                dfs(openN + 1, closeN)
                sol.pop()
            
            if closeN < openN:
                sol.append(")")
                dfs(openN, closeN + 1)
                sol.pop()
            
        dfs(0, 0)
        return ans