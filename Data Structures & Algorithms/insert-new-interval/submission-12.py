class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        * 題目核心: 給你一個 intervals 的區間。 這些區間是不會互相重疊，今天給你一個新的區間做插入，最後輸出的
        intervals 一樣要不會互相重疊。
        * 想法:
            * 有解: 
                * 直觀: 給你一個 newInterval, 看 start 落在哪裡，如果 start 比 interval[1] 還大，就直接加入 res
                ，如果找到一個 interval[1] >= start 代表這個 interval 會跟 newInterval 重疊，所以先不能加入到
                res 中，這時 start = min(start, interval[0])，這裡有一個要注意，因為很可能 newInterval 不會超過
                目前的 interval[1]，所以 end = max(end, interval[1]); 接下來去找 end 會擴展到哪裡，如果說
                end < _interval[0] 代表就是放在這個 _interval 前面， 如果 end >= _interval[0] 代表就會擴展下去，
                然後更新 end = max(end, interval[1])。 這時 start 與 end 都處裡好了，就直接插入res，最後再把剩下
                的 interval 插入到 res。
            * 無解: 不可能，頂多 intervals 可能是空的，那就直接把新的 intervals 插入即可。
        """


        res = []
        start, end = newInterval[0], newInterval[1]
        n = len(intervals)
 
        for i in range(n):
            interval = intervals[i]
            if interval[1] < start:
                res.append(interval)
            elif interval[0] <= end:
                start = min(start, interval[0])
                end = max(end, interval[1])
            else:
                res.append([start, end])
                for j in range(i, n):
                    res.append(intervals[j])
                return res

        res.append([start, end])

        return res

            