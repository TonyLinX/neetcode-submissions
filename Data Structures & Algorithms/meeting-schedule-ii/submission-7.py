"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        heap = []
        count = 0
        res = float("-inf")
        n = len(intervals)
        intervals.sort(key=lambda x: x.start)
        for i in range(0, n):
            while len(heap) >= 1 and heap[0] <= intervals[i].start:
                heapq.heappop(heap)
            heapq.heappush(heap, intervals[i].end)
            count = len(heap)
            res = max(res, count)

        return res if res!= float("-inf") else 0
        