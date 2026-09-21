class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        
        def topoSort(conditions):
            adj = [[] for i in range(k+1)]
            inDegree = [0] * (k+1)

            for u, v in conditions:
                adj[u].append(v)
                inDegree[v] += 1
            
            q = deque([i for i in range(1, k+1) if inDegree[i] == 0])
            res = []

            while q:
                node = q.popleft()
                res.append(node)

                for neig in adj[node]:
                    inDegree[neig] -= 1
                    if inDegree[neig] == 0:
                        q.append(neig)
            return res if len(res) == k else []
        
        rowOrder = topoSort(rowConditions)
        colOrder = topoSort(colConditions)

        if not rowOrder or not colOrder:
            return []

        rowMap = {num : i for i, num in enumerate(rowOrder)}
        colMap = {num : i for i, num in enumerate(colOrder)}
        matrix = [[0] * k for _ in range(k)]

        for i in range(1, k+1):
            ridx = rowMap[i]
            cidx = colMap[i]
            matrix[ridx][cidx] = i
        return matrix