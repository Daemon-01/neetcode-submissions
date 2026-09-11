class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)
        for i, euq in enumerate(equations):
            a, b = euq
            adj[a].append([b, values[i]])
            adj[b].append([a, 1 / values[i]])

        def evaluate(src, target):
            if src not in adj or target not in adj:
                return -1
            
            q, visit = deque(), set()
            q.append([src, 1])
            visit.add(src)

            while q:
                node, w = q.popleft()
                if node == target:
                    return w
                for neig, weight in adj[node]:
                    if neig not in visit:
                        q.append([neig, weight * w])
                        visit.add(neig)
            return -1

        return [evaluate(src, des) for src, des in queries]