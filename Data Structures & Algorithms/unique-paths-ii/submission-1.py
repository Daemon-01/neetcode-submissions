class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:

        def dfs(cur_row, cur_col):
            if (cur_row, cur_col) == (m-1, n-1) and grid[cur_row][cur_col] != 1:
                return 1
            if (cur_row == m or cur_col == n):
                return 0
            if grid[cur_row][cur_col] == 1:
                return 0
            if (cur_row, cur_col) in cache:
                return cache[(cur_row, cur_col)]
            
            count = 0
            count += dfs(cur_row+1, cur_col)
            count += dfs(cur_row, cur_col+1)
            
            cache[(cur_row, cur_col)] = count

            return count
        m, n = len(grid), len(grid[0])
        cache = {(m-1, n-1) : 1}
        return dfs(0, 0)