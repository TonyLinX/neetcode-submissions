class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        @ input: a single list
        @ output: a number
        * 選擇買跟賣的那天，那天必須是不同天，也可以不買賣
        """
        res = 0
        for i in range(len(prices)):
            buy = prices[i]
            for j in range(i+1, len(prices)):
                res = max(res, (prices[j]-buy))
        return res
        