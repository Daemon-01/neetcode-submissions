class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        grid = [[0 for _ in range(n+1)] for _ in range(m+1)]

        for row in range(1, m+1):
            row_char = text1[row-1]
            for col in range(1, n+1):
                col_char = text2[col-1]
                if row_char == col_char:
                    grid[row][col] = 1 + grid[row-1][col-1]
                else:
                    grid[row][col] = max(grid[row-1][col], grid[row][col-1])
        return grid[m][n]