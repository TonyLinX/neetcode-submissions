class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        @ input: a single list
        @ output: a number
        * 選擇買跟賣的那天，那天必須是不同天，也可以不買賣
        * 直觀想法就是雙層 for loop 可行但重複計算許多
        """
        # res = 0
        # for i in range(len(prices)):
        #     buy = prices[i]
        #     for j in range(i+1, len(prices)):
        #         res = max(res, (prices[j]-buy))
        # return res


        res = 0
        left, right = 0, 1
        while right < len(prices):
            if prices[right] - prices[left] < 0:
                left = right
            else:
                res = max(res, prices[right]-prices[left])
            right+=1
        return res