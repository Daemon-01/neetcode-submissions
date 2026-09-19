class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        cost = [float("inf")] * n
        cost[src] = 0

        for i in range(k+1):
            tmp = cost.copy()

            for u, v, price in flights:
                if cost[u] != float("inf") and cost[u] + price < tmp[v]:
                    tmp[v] = cost[u] + price
            cost = tmp
        return cost[dst] if cost[dst] != float("inf") else -1