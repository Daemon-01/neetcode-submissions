class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        visited = set()

        def dfs(r, c, visited):
            if(r < 0 or c < 0 or r >= rows or c >= cols or
                board[r][c] == "X" or (r, c) in visited):
                return
            
            visited.add((r, c))

            dfs(r + 1, c, visited)
            dfs(r - 1, c, visited)
            dfs(r, c + 1, visited)
            dfs(r, c - 1, visited)

        for r in range(rows):
            for c in range(cols):
                if (r == 0 or c == 0 or r == rows-1 or c == cols-1):
                    dfs(r, c, visited)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r, c) not in visited:
                    board[r][c] = "X" 