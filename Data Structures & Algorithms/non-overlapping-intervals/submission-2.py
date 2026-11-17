class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        * 題目核心: 給你一個可能有 overlapping 的 intervals，回傳最少需要刪除多少個
        intervals 才會變成不 overlapping。
        * 想法:
            * 有解: 假設是[1,5]、[2,3]、[3,4]，我們可以刪 [1,5]保留[2,3]，也可以
            倒過來，但是如說保留[1,5]，[3,4]還是跟它重疊。所以當重疊的時候，到底要
            刪哪一個，取決於end 的大小，留著 end 比較小的那一個，因為代表那個interval
            比較早結束，更難重疊到下一個。所以整個實作一樣，先排序，然後用第0個interval
            的 end 作為初始 end，然後從第 1 個 interval 開始比，比的過程只會有兩種
            情況 (重疊跟不重疊)，不重疊就 end 就直接等於下一個 interval 的end，如果
            重疊就是 end 會是這兩個interval最小的end，然後count+=1。 那複雜度為
            t:O(nlogn), s:O(n)
            * 無解: 不可能頂多就是 1 個，直接回傳 0。
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