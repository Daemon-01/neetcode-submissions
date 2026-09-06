class Solution:
    # 1. Define the separate helper class inside the Solution class
    class DisjointSet:
        def __init__(self, size: int):
            self.parent = [i for i in range(size)]
            self.rank = [1] * size

        def find(self, i: int) -> int:
            if self.parent[i] == i:
                return i
            self.parent[i] = self.find(self.parent[i])  # Path compression
            return self.parent[i]

        def union(self, i: int, j: int) -> bool:
            root_i = self.find(i)
            root_j = self.find(j)

            if root_i == root_j:
                return False  # Cycle detected!

            # Union by Rank
            if self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            elif self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            else:
                self.parent[root_j] = root_i
                self.rank[root_i] += 1
            return True

    # 2. Main LeetCode function
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        # A valid tree with 'n' nodes MUST have exactly 'n - 1' edges.
        if len(edges) != n - 1:
            return False
            
        # Instantiate the nested class using self.DisjointSet
        dsu = self.DisjointSet(n)
        
        # Loop through edges to check for cycles
        for u, v in edges:
            if not dsu.union(u, v):
                return False  # Redundant connection found -> Cycle exists!
                
        return True
