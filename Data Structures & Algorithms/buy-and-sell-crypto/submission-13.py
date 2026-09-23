class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        * 題目目標是找到 maximum profit。
        * 暴力解是 O(n^2) => 雙 for loop 計算所有可能
        * O(n) 的解法其實，找到最低點去買，然後計算後續天比買那天還高的利益。 =>
          一個 for 迴圈，兩個參數(buy_day, sell_day): 從第0個元素開始， 只要後面元素比 buy_day 那天
          的價格還要大，就計算利益，保留最大利益作為結果。當後面元素比buy_day 那天的價格還要小，直接將
          buy_day 換成這一天。 因為比前面還大的利益只會出現在更低的買點，所以可以直接丟掉舊的 
          buy_day。
        * 犯錯:
            * 第二次(9/23): enumerate 不能指定從某一個元素開始，只有 range 才可以
        """

        res = 0
        buy_day = 0

        for sell_day in range(1, len(prices)):
            value = prices[sell_day]
            if value >= prices[buy_day]:
                res = max(res, value - prices[buy_day])
            else:
                buy_day = sell_day

        
        return res
            
        

    