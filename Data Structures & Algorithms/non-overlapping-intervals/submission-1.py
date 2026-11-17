class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        * 題目核心:
        * 想法:
            * 有解:
            * 無解:不可能頂多就是 1 個，直接回傳 0。
        """
        n = len(intervals)
        if n == 1:
            return 0
        
        intervals.sort()
        end = intervals[0][1]
        res = 0

        for i in range(1, n):
            # 沒重疊
            if end <= intervals[i][0]:
                end = intervals[i][1]
            # 重疊
            else:
                end = min(end, intervals[i][1])
                res += 1



        return res