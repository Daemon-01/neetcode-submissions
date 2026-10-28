class Solution:
   def minPathSum(self, grid):
    m, n = len(grid), len(grid[0])
    memo = {}

    def solve(r, c):
        if r == m or c == n:
            return float("inf")
        if (r, c) == (m - 1, n - 1):
            return grid[r][c]
        if (r, c) in memo:
            return memo[(r, c)]

        memo[(r, c)] = grid[r][c] + min(solve(r + 1, c), solve(r, c + 1))
        return memo[(r, c)]

    return solve(0, 0)