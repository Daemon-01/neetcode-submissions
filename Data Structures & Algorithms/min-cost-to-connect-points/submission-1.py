import heapq

class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        n = len(points)
        adj = {i : [] for i in range(n)} # i : list of [dis, route]

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                dis = abs(x1-x2) + abs(y1-y2)
                adj[i].append([dis, j])
                adj[j].append([dis, i])
        
        res = 0
        visit = set()
        minHeap = [[0,0]]  # [cost, node]

        while len(visit) < n:
            cost, i = heapq.heappop(minHeap)
            if i in visit:
                continue
            res += cost 
            visit.add(i)

            for neigCost, neig in adj[i]:
                if neig not in visit: 
                    heapq.heappush(minHeap, [neigCost, neig])
                    
        return res
