class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        * 題目核心: 給你一個 intervals，輸出一個完全不重疊且完全涵蓋原本區間的 intervals。
        * 想法:
            * 有解: 從第一個 intervals 開始 for loop，將 start, end 初始化為第一個 intervals的，
            第 0 與 第 1 個元素，不重疊只會兩種情況，就是 start 與 end 比下一個 interval 的 start 都
            還小，或者 start 與 end 比下一個 interval 的 end 還大，透過排序也就是字典敘的方式，可以避免
            第二種情況發生，簡單化整個題目。實作:讓所有 intervals 的 start 是由小到大，如果 start 一樣，
            再比 end 由小到大。  所以說如果第一種情況，直接將 [start, end]加入到 result，然後下一個
            interval 的 start 與 end 做為新的 start 與 end， 並且 i+=1 從下下個開始比。如果說有重疊，
            start 取最小值，end 取最大值。最後整個for loop 結束，就要把最後 start , end 放到 result.
            * 無解: 不可能，intervals 最小 1個，那就是直接輸出那個 interval。
        """
        # 這個排序叫做根據你自己想要比較的值去做排序，這就是根據 intervals[0] 去排序
        # intervals.sort(key=lambda x: x[0])
        # 這是python的排序，針對二維 list 他會先比較intervals[0]由小到大，再去比intervals[1] 由小到大
        # 稱為字典序。
        intervals.sort()

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

    