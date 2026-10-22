class Solution:
    def climbStairs(self, n: int) -> int:
        """
        *   這題核心是給你一個 n  代表你要走幾步才可以走到樓梯的頂端。你每一次可以走 1 步 or 2 步，最後回傳
        走到頂端的方式數量。
        """
        if n == 1:
            return 1
        if n == 2:
            return 1+1
    
        dp = [0]*(n+1)    
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]
