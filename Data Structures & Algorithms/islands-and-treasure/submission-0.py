class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visit.add((r,c))

        def addRoom(r, c):
            if (r < 0 or c < 0 or 
                r == rows or c == cols or grid[r][c] == -1 or
                (r,c) in visit):
                return 

            visit.add((r,c))
            q.append((r,c))

        dis = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = dis

                addRoom(r+1, c) # down
                addRoom(r-1, c) # up
                addRoom(r, c+1) # right
                addRoom(r, c-1) # left
            dis += 1