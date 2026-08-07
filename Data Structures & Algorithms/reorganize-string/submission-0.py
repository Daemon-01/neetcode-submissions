class Solution:
    def reorganizeString(self, s: str) -> str:
        charMap = Counter(s)
        maxHeap = [(-count, char) for char, count in charMap.items()]
        heapq.heapify(maxHeap)

        prevCount, prevChar = 0, ""
        res = []

        while maxHeap:
            count, char = heapq.heappop(maxHeap)
            res.append(char)

            count += 1

            if prevCount < 0:
                heapq.heappush(maxHeap, (prevCount, prevChar))
            
            prevCount, prevChar = count, char
        
        output = "".join(res)

        return output if len(res) == len(s) else ""