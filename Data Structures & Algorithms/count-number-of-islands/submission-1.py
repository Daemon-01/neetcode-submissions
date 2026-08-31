class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # optimized version 
        # uses O(1) space, modify the grid itself
        islandCount = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if (r < 0 or c < 0 or
                r >= rows or c >= cols or
                grid[r][c] != "1"):
                return
            
            grid[r][c] = "#"

            dfs(r+1, c)
            dfs(r, c+1)
            dfs(r-1, c)
            dfs(r, c-1)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" :
                    islandCount += 1
                    dfs(r, c)
        return islandCount