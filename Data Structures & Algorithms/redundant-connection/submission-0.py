class Solution:
    class Disjoint:
        def __init__(self, size):
            self.parent = [i for i in range(size)]
            self.rank = [0] * size
        
        def find(self, i):
            if self.parent[i] == i:
                return i
            self.parent[i] = self.find(self.parent[i])
            return self.parent[i]
        
        def Union(self, i, j):
            rootI = self.find(i)
            rootJ = self.find(j)

            if rootI == rootJ:
                return False
            
            if self.rank[rootI] > self.rank[rootJ]:
                self.parent[rootJ] = rootI
            elif self.rank[rootI] < self.rank[rootJ]:
                self.parent[rootI] = rootJ
            else:
                self.parent[rootJ] = rootI
                self.rank[rootI] += 1
            
            return True

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        dsu = self.Disjoint(n)

        for u, v in edges:
            if not dsu.Union(u, v):
                return [u,v]