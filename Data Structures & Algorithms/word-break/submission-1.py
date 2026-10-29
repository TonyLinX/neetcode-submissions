class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}
        dp[len(s)] = True

        def dfs(i: int) -> bool:
            if i in dp:
                return dp[i]

            for word in wordDict:
                if word == s[i: i + len(word)]:
                    dp[i] = dfs(i+len(word))

                    if dp[i]:
                        return dp[i]
            dp[i] = False

            return dp[i]

        dp[0] = dfs(0)
        
        return dp[0]