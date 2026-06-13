class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqCount = {}

# for creating the dictionary that will track the freq of the elments
        for num in nums:
            freqCount[num] = freqCount.setdefault(num,0) + 1
        result = []

        heap = [(-count , char) for char , count in freqCount.items()]
        heapq.heapify(heap)

        for _ in range(0,k):
            element = heapq.heappop(heap)[1]
            result.append(element)
        return result

