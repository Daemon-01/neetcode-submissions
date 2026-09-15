class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for p1, p2 in tickets:
            heapq.heappush(adj[p1], p2)
        res = []
        stack = ["JFK"]

        def dfs(airport):
            while adj[airport]:
                nextAir = heapq.heappop(adj[airport])
                dfs(nextAir)
            res.append(airport)
        dfs("JFK")
        return res[::-1]           