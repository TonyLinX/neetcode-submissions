class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        *   核心: 給你硬幣的面額以及給你有多少錢，要你回傳最少可以代表這個面額的硬幣數量。如果沒辦法用現有的面額
                去得到對應的錢就是回傳 -1。
        *   想法:
            *   暴力解 (答案記錄在外面): 可以用 decision tree，去找到合法的解，然後記錄最少的那個組合。
                可以用遞回來實現。
                - dfs(remain, count) remain 代表剩下多少錢，count 代表目前此組合的硬幣數量。
                - base case 為 reamin == 0 
                - 遞迴關係 只要面額小等於剩下的錢就繼續遞迴。
            *   暴力解(回傳型): 一樣用 recursion來實現。
                - dfs(remain) remain 代表剩下的錢最少可以使用幾個硬幣代表。
                - base case 為 remain == 0 回傳 0 代表剩下 0 元，就是0 個硬幣就能代表。
                - 遞迴關係 只要面額小等於剩下的錢就繼續遞迴。
                - 複雜度：每個 dfs 試 k 種硬幣，節點數每層乘 k；最多 amount 層（一直用面額 1）。
                T: O(k^amount)，指數級會 TLE；S: O(amount)，遞迴最多疊 amount 層。 那 amount 最大 10000
                所以絕對會TLE。
            *   最優解(dp): 可以發現，會有許多dfs(remain)被重複計算的地方。 所以可以透過 memory 記起來。
                - 用一個 set 去記錄此 remain 是否已經計算過，如果有就直接回傳，沒有就遞迴
                - 用一個 amount + 1 長度的 array 紀錄每一個剩下的金額最少的硬幣數量
                
        """
        # 暴力解(遍歷型)
        # if amount == 0:
        #     return 0

        # resCount = float("inf")
        
        # def dfs(remain: int, count: int) -> None:
        #     nonlocal resCount
        #     if remain == 0:
        #         if count < resCount:
        #             resCount = count
        #         return
            
        #     for coin in coins:
        #         if coin <= remain:
        #             dfs(remain-coin, count+1)            

        # dfs(amount, 0)

        # return resCount if resCount != float("inf") else -1

        #暴力解(回傳型)

        # def dfs(remain: int)->int :
        #     if remain == 0:
        #         return 0
            
        #     cur = float("inf")
        #     for coin in coins:
        #         if coin <= remain:
        #             temp = dfs(remain-coin)
        #             if temp != -1:
        #                 cur = min(cur, temp)

        #     if cur == float("inf"):
        #         return -1

        #     return cur + 1

        # return dfs(amount)

        # 次優解(dp, Top-Down)
        
        dp = [float("inf")] * (amount + 1)
        dp_set = set()
        dp[0] = 0
        dp_set.add(0)

        def dfs(remain: int)->int :
            if remain in dp_set:
                return dp[remain]

            for coin in coins:
                if coin <= remain:
                    temp = dfs(remain-coin)
                    print(remain, temp)
                    if temp != -1:
                        dp[remain] = min(dp[remain], temp + 1)

            dp_set.add(remain)

            if dp[remain] == float("inf"):
                dp[remain] = -1

            return dp[remain]

        dp[amount] = dfs(amount)
        
        return dp[amount]

        