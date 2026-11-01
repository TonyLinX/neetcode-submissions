class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        

        dp_set = set()
        dp = [[0] * len(text2) for _ in range(len(text1))]
        
        def dfs(i: int, j: int) -> int:
            if i == len(text1) or j == len(text2):
                return 0

            if (i,j) in dp_set:
                return dp[i][j]

            if text1[i] == text2[j]:
                dp[i][j] = 1 + dfs(i+1, j+1)
            else:
                dp[i][j] = max(dfs(i+1, j), dfs(i, j+1))
            
            dp_set.add((i,j))
            

            return dp[i][j]

        dp[0][0] = dfs(0, 0)


        return dp[0][0]
            