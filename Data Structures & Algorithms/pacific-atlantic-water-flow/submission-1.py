class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pacific_visited = set()
        atlantic_visited = set()

        def dfs(r, c, prev_height, visited):
            if (r < 0 or c < 0 or r >= rows or c >= cols or
                (r, c) in visited or heights[r][c] < prev_height):
                return 
            
            visited.add((r,c))

            dfs(r + 1, c, heights[r][c], visited)
            dfs(r - 1, c, heights[r][c], visited)
            dfs(r , c + 1, heights[r][c], visited)
            dfs(r , c - 1, heights[r][c], visited)

        for r in range(rows):
            dfs(r, 0, heights[r][0], pacific_visited) # pacific left
            dfs(r, cols-1, heights[r][cols-1], atlantic_visited) # atlantic right

        for c in range(cols):
            dfs(0, c, heights[0][c], pacific_visited) # pacific top
            dfs(rows-1, c, heights[rows-1][c], atlantic_visited) # atlantic down
        
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific_visited and (r, c) in atlantic_visited:
                    res.append([r, c])
        
        return res