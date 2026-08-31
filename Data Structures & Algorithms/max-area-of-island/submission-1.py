class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if (r < 0 or c < 0 or
                r >= rows or c >= cols or 
                grid[r][c] != 1):
                return 0
            
            grid[r][c] = "#"

            area = (
                1 +
                dfs(r + 1, c) +
                dfs(r, c + 1) +
                dfs(r - 1, c) +
                dfs(r, c - 1)
            )

            return area
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    islandArea = dfs(r, c)
                    maxArea = max(islandArea, maxArea)
        return maxArea
