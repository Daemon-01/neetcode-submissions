class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pacific_visited = set()
        atlantic_visited = set()

        def dfs(r, c, visited, prev_height):
            # Guard conditions: boundaries, already visited, or flowing downhill inland (invalid)
            if (r < 0 or c < 0 or r >= rows or c >= cols or 
                (r, c) in visited or heights[r][c] < prev_height):
                return
            
            visited.add((r, c))
            
            # Flood inland to all 4 neighbors
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])

        # 1. Flood from Top and Bottom borders
        for c in range(cols):
            dfs(0, c, pacific_visited, heights[0][c])            # Pacific (Top)
            dfs(rows - 1, c, atlantic_visited, heights[rows-1][c]) # Atlantic (Bottom)

        # 2. Flood from Left and Right borders
        for r in range(rows):
            dfs(r, 0, pacific_visited, heights[r][0])            # Pacific (Left)
            dfs(r, cols - 1, atlantic_visited, heights[r][cols-1]) # Atlantic (Right)

        # 3. Find cells present in BOTH ocean sets
        result = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific_visited and (r, c) in atlantic_visited:
                    result.append([r, c])

        return result
