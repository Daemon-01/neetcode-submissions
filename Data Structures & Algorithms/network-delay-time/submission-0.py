class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list) # maps the node to next node with weight
        visit = set()
        time = 0

        for nodes in times:
            u, v, w = nodes[0], nodes[1], nodes[2]
            adj[u].append((v, w))
        
        minHeap = [[0,k]]

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            visit.add(n1)
            time = max(time, w1)

            for n2, w2 in adj[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, [w1 + w2, n2])
        return time if len(visit) == n else -1
            