class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        if not grid:
            return 0
            
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_oranges = 0
        minutes_elapsed = 0
        
        # 1. Multi-source Initialization
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c)) # Add all rotten oranges to start together
                elif grid[r][c] == 1:
                    fresh_oranges += 1
                    
        # If there are no fresh oranges to begin with, 0 minutes are needed
        if fresh_oranges == 0:
            return 0
            
        # Directions for moving Up, Down, Left, Right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # 2. Level-by-Level Multi-source BFS
        while queue and fresh_oranges > 0:
            minutes_elapsed += 1
            
            # Process all oranges rotting at the current minute mark
            for _ in range(len(queue)):
                r, c = queue.popleft()
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    
                    # 3. The Condition Shift: Only touch valid, FRESH oranges
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2       # Rot the orange (acts as "visited")
                        fresh_oranges -= 1    # Decrement remaining fresh count
                        queue.append((nr, nc)) # It will rot its neighbors next minute
                        
        # 4. Final Verification
        return minutes_elapsed if fresh_oranges == 0 else -1

            