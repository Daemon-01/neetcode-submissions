class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        edgeCount = {}
        q = deque()
        for src, neighbors in adj.items():
            if len(neighbors) == 1:
                q.append(src)
            edgeCount[src] = len(neighbors)
        
        while q:
            if n <= 2:
                return list(q)
            for i in range(len(q)):
                n -= 1
                node = q.popleft()
                for neig in adj[node]:
                    edgeCount[neig] -= 1
                    if edgeCount[neig] == 1:
                        q.append(neig)