"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        
        
        intervals.sort(key=lambda x:(x.start, x.end))
        n = len(intervals)

        if n == 0:
            return True
        
        start, end = intervals[0].start, intervals[0].end
        for i in range(1, n):
            _interval = intervals[i]
            if start <= _interval.start and end <= _interval.start:
                start, end = _interval.start, _interval.end
                continue
            else:
                return False

        return True 

         