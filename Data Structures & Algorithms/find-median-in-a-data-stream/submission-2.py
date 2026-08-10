class MedianFinder:

    def __init__(self):
        self.smaller = [] # maxHeap for storing small elements
        self.larger = [] # minHeap for storing the max elements

    def addNum(self, num: int) -> None:
        if self.larger and self.larger[0] < num:
            heapq.heappush(self.larger, num)
        else:
            heapq.heappush(self.smaller, -num)

        if len(self.smaller) > len(self.larger) + 1:
            val = -heapq.heappop(self.smaller)
            heapq.heappush(self.larger, val)
        elif len(self.smaller) + 1 < len(self.larger):
            val = -heapq.heappop(self.larger)
            heapq.heappush(self.smaller, val)

    def findMedian(self) -> float:
        if len(self.smaller) > len(self.larger):
            return -self.smaller[0]
        elif len(self.smaller) < len(self.larger):
            return self.larger[0]
        else:
            return (-self.smaller[0] + self.larger[0]) / 2
        