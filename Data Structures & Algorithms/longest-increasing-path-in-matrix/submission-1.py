class Solution:
    def longestIncreasingPath(self, grid: List[List[int]]) -> int:
        caching = {}
        best = 0
        rows, cols = len(grid), len(grid[0])
        
        def maxpath(num, r, c, count):
            if (r, c) in caching:
                return caching[(r, c)]

            longest = 1

            if r+1 < rows and grid[r+1][c] > num:
                longest = max(longest, 1 + maxpath(grid[r+1][c], r+1, c, count))
            if r-1 >= 0 and grid[r-1][c] > num:
                longest = max(longest, 1 + maxpath(grid[r-1][c], r-1, c, count))
            if c+1 < cols and grid[r][c+1] > num:
                longest = max(longest, 1 + maxpath(grid[r][c+1], r, c+1, count))
            if c-1 >= 0 and grid[r][c-1] > num:
                longest = max(longest, 1 + maxpath(grid[r][c-1], r, c-1, count))
            
            caching[(r, c)] = longest
            return longest

        for r in range(rows):
            for c in range(cols):
                best = max(best, maxpath(grid[r][c], r, c, 0))
        return best