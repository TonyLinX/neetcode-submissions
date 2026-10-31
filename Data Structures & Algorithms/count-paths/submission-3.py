class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp_set = set()
        dp = [[0] * n for _ in range(m)]

        dp[m-1][n-1] = 1
        dp_set.add((m-1, n-1))

        def dfs(i: int, j:int) -> int:
            if (i,j) in dp_set:
                return dp[i][j]

            down = right = 0
            # 往下/右
            if i+1 < m:
                down = dfs(i+1, j)
            if j+1 < n:
                right = dfs(i, j+1)
            
            dp[i][j] = down + right
            dp_set.add((i,j))

            return dp[i][j]
        dp[0][0] = dfs(0, 0)

        return dp[0][0]


        