import heapq
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        
        for x, y in points:
            dist = x**2 + y**2  # No need for sqrt
            
            if len(max_heap) < k:
                heapq.heappush(max_heap, (-dist, [x, y]))
            elif -dist > max_heap[0][0]:
                heapq.heappushpop(max_heap, (-dist, [x, y]))
        
        return [point for _, point in max_heap]