class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        if len(self.small) == 0 or num <= -self.small[0]:
            heapq.heappush(self.small, -num)
            if len(self.small) > len(self.large) + 1:
                temp = heapq.heappop(self.small)
                heapq.heappush(self.large, -temp)
        else:
            heapq.heappush(self.large, num)
            if len(self.large) > len(self.small):
                temp = heapq.heappop(self.large)
                heapq.heappush(self.small, -temp)

    def findMedian(self) -> float:
        k = len(self.small) + len(self.large)
        if k % 2 == 0:
            return (-self.small[0] + self.large[0]) / 2
        else:
            return -self.small[0]