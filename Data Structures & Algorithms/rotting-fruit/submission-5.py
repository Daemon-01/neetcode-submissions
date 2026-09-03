class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        freshOranges = 0
        visit = set()
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                    visit.add((r,c))
                elif grid[r][c] == 1:
                    freshOranges += 1
        
        def nextRottenOranges(r, c):
            if(r < 0 or c < 0 or 
                r == rows or c == cols or grid[r][c] == 0 or 
                (r, c) in visit):
                return
            q.append((r,c))
            visit.add((r,c))
        
        minTime = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()

                if grid[r][c] == 1:
                    grid[r][c] = minTime
                    freshOranges -= 1
                
                nextRottenOranges(r+1, c)
                nextRottenOranges(r-1, c)
                nextRottenOranges(r, c+1)
                nextRottenOranges(r, c-1)
            if q:
                minTime += 1
        return minTime if freshOranges == 0 else -1