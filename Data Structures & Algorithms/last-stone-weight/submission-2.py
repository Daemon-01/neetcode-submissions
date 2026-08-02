class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap)

        while (len(heap) > 1):
            stone1, stone2 = -heapq.heappop(heap), -heapq.heappop(heap)
            if stone1 != stone2:
                newStone = abs(stone1-stone2)
                heapq.heappush(heap, -newStone)
        return -heap[0] if heap else 0