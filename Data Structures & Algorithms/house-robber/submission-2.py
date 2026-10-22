class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        *   這題核心就是給你一個 int list，裡面代表同一排每一棟房子的錢，在不能連續搶劫兩棟房子的情況下，回傳最大可以搶多少錢。
        *   想法:
            *   有解: 搶的方式可以有很多種，最值觀的想法就是列出所有搶劫的方式，然後持須更新最多可以搶多少錢，這就是答案。找出所有搶劫方式
            可以透過 recursion 來實現。那我們可以思考其實有許多的子問題，是已經被計算過了，所以說可以把答案記錄起來，不用再算一次，這樣的方
            法就是 DP。 搶到第 n 棟時，其實就分成搶與不搶:
                * 搶: 代表是 H(4) + H(2) # 因為不能連續搶兩棟
                * 不搶: 代表是 H(3)
                => H(4) = max(H(4) + H(2), H(3))
            *   無解: 不可能，因為最少一棟，一樣回傳最多可以搶多少錢。
        """

        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums[0], nums[1])
        

        dp = [0]*len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        res = dp[1]

        for i in range(2, len(nums)):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
            res = max(res, dp[i])


        return res 

        