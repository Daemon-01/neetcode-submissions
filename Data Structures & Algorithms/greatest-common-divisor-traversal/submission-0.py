class UnionFind:
    def __init__(self):
        self.par = {}
        self.rank = {}

    def find(self, i):
        if i not in self.par:
            self.par[i] = i
            self.rank[i] = 1
            return i
        if self.par[i] == i:
            return i
        self.par[i] = self.find(self.par[i])
        return self.par[i]

    def union(self, i, j):
        p1, p2 = self.find(i), self.find(j)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
        else:
            self.par[p2] = p1
            self.rank[p1] += 1
        return True


class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        uf = UnionFind()

        def factorize(x):
            factors = []
            d = 2
            while d * d <= x:
                if x % d == 0:
                    factors.append(d)
                    while x % d == 0:
                        x = x // d
                d += 1
            if x > 1:
                factors.append(x)
            return factors

        for i, num in enumerate(nums):
            if num == 1:
                return False
            for p in factorize(num):
                uf.union(i, p)

        root0 = uf.find(0)
        return all(uf.find(i) == root0 for i in range(len(nums)))