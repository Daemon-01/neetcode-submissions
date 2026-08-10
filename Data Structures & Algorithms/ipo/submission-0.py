class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = sorted(zip(capital, profits))
        maxHeap = []
        idx = 0

        for _ in range(k):
            while idx < len(projects) and projects[idx][0] <= w:
                heapq.heappush(maxHeap, -projects[idx][1])
                idx += 1

            if not maxHeap:
                break

            w += -heapq.heappop(maxHeap)
        return w