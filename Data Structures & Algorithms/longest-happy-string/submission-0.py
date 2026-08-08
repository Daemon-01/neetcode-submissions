class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = []
        maxHeap = []

        for count, char in [(-a, 'a'), (-b, "b"), (-c, "c")]:
            if count < 0:
                maxHeap.append((count, char))
    
        heapq.heapify(maxHeap)

        while maxHeap:
            count, char = heapq.heappop(maxHeap)

            if len(res) >= 2 and res[-1] == char and res[-2] == char:
                if not maxHeap:
                    break
                
                nextCount, nextChar = heapq.heappop(maxHeap)
                res.append(nextChar)
                nextCount += 1

                if nextCount < 0:
                    heapq.heappush(maxHeap, (nextCount, nextChar))
            
            else:
                res.append(char)
                count += 1

            if count < 0:
                heapq.heappush(maxHeap, (count, char))
        return "".join(res)
            