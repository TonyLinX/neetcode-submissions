class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Top down
        # dp = {}
        # dp[len(s)] = True

        # def dfs(i: int) -> bool:
        #     if i in dp:
        #         return dp[i]

        #     for word in wordDict:
        #         if word == s[i: i + len(word)]:
        #             dp[i] = dfs(i+len(word))

        #             if dp[i]:
        #                 return dp[i]
        #     dp[i] = False

        #     return dp[i]

        # dp[0] = dfs(0)

        # return dp[0]


        # bottom up
        dp = {i: False for i in range(len(s) + 1)}
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                # 2. 遞推公式：word 剛好接在 i 開頭（逐字比對），
                #    而且接完之後的位置能切完 → dp[i] = True
                if s[i : i + len(word)] == word and dp[i + len(word)]:
                    dp[i] = True
                    break  
        return dp[0]
