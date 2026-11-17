class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        * 題目核心: 給你一個 intervals，輸出一個完全不重疊且完全涵蓋原本區間的 intervals。
        * 想法:
            * 有解: 從第一個 intervals 開始 for loop，將 start, end 初始化為第一個 intervals的，
            第 0 與 第 1 個元素，不重疊只會兩種情況，就是 start 與 end 比下一個 interval 的 start 都
            還小，或者 start 與 end 比下一個 interval 的 end 還大，但原本是 intervals，所以不會出現
            第二種情況，如果真的有就是先排序，讓所有 intervals 的 start 是由小到大，如果 start 一樣，
            再比 end 由小到大。 那目前我們就不先考慮。 所以說如果第一種情況，直接將 [start, end]加入
            到 result，然後下一個 interval 的 start 與 end 做為新的。如果說有重疊，start 取最小值，
            end 取最大值。
            * 無解: 不可能，intervals 最小 1個，那就是直接輸出那個 interval。
        """

        intervals.sort(key=lambda x: x[0])
        
        result = []

        start, end = intervals[0][0], intervals[0][1]
        n = len(intervals)

        for i in range(1, n):
            if start < intervals[i][0] and end < intervals[i][0]:
                result.append([start, end])
                start,end = intervals[i][0], intervals[i][1]
                i += 1
            else:
                start = min(start, intervals[i][0])
                end = max(end, intervals[i][1])
            
        
        result.append([start, end])

        return result

    