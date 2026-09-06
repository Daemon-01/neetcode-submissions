class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        # A valid tree with 'n' nodes MUST have exactly 'n - 1' edges.
        # If it doesn't, it's either disconnected or contains an obvious cycle.
        if len(edges) != n - 1:
            return False
            
        # Initialize your DSU structures directly here
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
        
        # 1. Corrected Find Function (removed 'size', added 'self.')
        def find(i: int) -> int:
            if self.parent[i] == i:
                return i
            self.parent[i] = find(self.parent[i]) # Path compression
            return self.parent[i]
        
        # 2. Corrected Union Function (removed 'size', fixed variable names and 'self.')
        def union(i: int, j: int) -> bool:
            root_i = find(i)
            root_j = find(j)

            if root_i == root_j:
                return False # Cycle detected!
            
            # Union by Rank logic using self.rank and self.parent
            if self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            elif self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            else:
                self.parent[root_j] = root_i
                self.rank[root_i] += 1
            return True

        # 3. Main Algorithm Execution Loop
        for u, v in edges:
            if not union(u, v):
                return False # If union returns False, u and v were already connected (Cycle!)
                
        return True
