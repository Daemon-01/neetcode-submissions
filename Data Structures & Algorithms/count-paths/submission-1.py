class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = {(m-1,n-1) : 1}
        def dfs(cur_row, cur_col):
            if (cur_row, cur_col) in cache:
                return cache[(cur_row, cur_col)]
            if (cur_row == m or cur_col == n):
                return 0

            count = 0

            count += dfs(cur_row+1, cur_col)
            count += dfs(cur_row, cur_col+1)

            cache[(cur_row, cur_col)] = count
            return count
        return dfs(0, 0)