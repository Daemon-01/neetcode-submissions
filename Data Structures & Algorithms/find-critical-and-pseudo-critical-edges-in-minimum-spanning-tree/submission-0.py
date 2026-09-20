class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n
    
    def find(self, i):
        if self.par[i] == i:
            return i
        self.par[i] = self.find(self.par[i])
        return self.par[i]
    
    def Union(self, i, j):
        p1, p2 = self.find(i), self.find(j)

        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else :
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        for i, e in enumerate(edges):
            e.append(i)
        edges.sort(key=lambda x : x[2])

        mst_weight = 0
        unf = UnionFind(n)
        for u, v, w, i in edges:
            if unf.Union(u, v):
                mst_weight += w

        critical, pseudo = [], []
        # finding the critical and pseudo critical edges
        for u, v, w, i in edges:
            unf = UnionFind(n)
            weight = 0
            for n1, n2, wei, j in edges:
                if j != i and unf.Union(n1, n2):
                    weight += wei
            if max(unf.rank) != n or weight > mst_weight:
                critical.append(i)
                continue
                        
            unf = UnionFind(n)
            weight = w
            unf.Union(u, v)
            for n1, n2, wei, j in edges:
                if unf.Union(n1, n2):
                    weight += wei
            if weight == mst_weight:
                pseudo.append(i)
        return [critical, pseudo]