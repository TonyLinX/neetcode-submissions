class Solution:
    def numDecodings(self, s: str) -> int:
        """
        *   核心: 給一個只有數字的字串 s，每一段數字對應一個字母（1→A ... 26→Z），問總共有幾種切法。
        *   想法:
            *   有解:
                *   暴力解:
                    1. 先看「合法的一段」長什麼樣子：
                        - 1 位數：1 ~ 9（"0" 單獨一段沒有字母）
                        - 2 位數：10 ~ 26（"05" 這種 leading zero 不行）
                        - 3 位數以上：一定 > 26，不合法
                    → 所以每一段只可能是 1 位或 2 位。
                    2. 因此可以從左往右切，每個位置只有兩個選擇：切 1 位、或切 2 位。
                    會分岔、走完一條要回來走另一條 → 用 recursion（decision tree）。
                    3. 定義 dfs(i) = 從 index i 切到結尾，剩下的字串有幾種切法。答案是 dfs(0)。
                    4. base case（能直接決定整個 dfs(i) 答案的情況）:
                        - i == n：前面每段都合法、剛好切完 → 這是一種成功的切法，回傳 1
                        - s[i] == "0"：切 1 位是 "0"、切 2 位是 "0X"，兩條路都不合法 → 回傳 0
                    5. 遞迴關係（兩個選擇是不同的切法，所以方法數相加）:
                        - 切 1 位：s[i] 不是 0（base case 已擋掉）→ 一定合法，加 dfs(i+1)
                        - 切 2 位：只有 s[i:i+2] 真的是一個字母（10 ~ 26）才能把它當一段 → 才加 dfs(i+2)
                        （這個條件只影響「切 2 位」這個選擇，切 1 位可能還是合法，所以不能當 base case，例如 "27" = 2|7）
                        => dfs(i) = dfs(i+1) + (s[i:i+2] 在 10 ~ 26 ? dfs(i+2) : 0)
                    6. 驗證 "112"：dfs(3)=1，dfs(2)=1，dfs(1)=dfs(2)+dfs(3)=2，dfs(0)=dfs(1)+dfs(2)=3 ✓
                    7. 複雜度：每個位置最多分 2 條路，T: 最差約 O(2^n)；S: O(n)，遞迴深度。
                    8. 問題：同一個 dfs(i) 會被不同路徑重複呼叫。
                    例如 "1112"：1|1|... 和 11|... 都會走到 dfs(2)，dfs(2) 算 2 次、dfs(3) 算 3 次。
                    → 下一步：把算過的 dfs(i) 記下來（memo），就是 DP。
                *   DP（top-down，memoization）:
                    9. 定義、base case、遞迴關係都跟暴力解一樣，只多一件事：每個 dfs(i) 算完就記下來。
                        - dp[i] 存 dfs(i) 的答案，dp_set 記哪些 i 已經算過
                        - 進 dfs(i) 先查：i 在 dp_set 裡 → 直接回傳 dp[i]，底下那整棵不再展開
                        - 沒算過 → 照遞迴關係算，存進 dp[i]、加入 dp_set，再回傳
                    10. 為什麼需要 dp_set：dp[i] = 0 有兩種意思（還沒算、算完答案就是 0，例如 "06"），只看 dp[i] 分不出來。
                    11. 複雜度（不同子問題數量 × 每個子問題的工作量）:
                        - 子問題 dfs(0) ~ dfs(n) 共 n+1 個，每個只算一次；每個只看一兩個字、做一次加法 O(1)
                        - T: O(n)；S: O(n)，dp、dp_set、遞迴深度。
            *   無解: 不存在無解的情況，沒有任何合法切法時回傳 0（例如 "06"）。
        *   觀念:
            *   暴力列舉所有切法 → 加剪枝（不合法的一段就不往下走）→ 加 memo（重複的子問題只算一次）= DP。
            *   條件只影響其中一個選擇 → 放在那個選擇的 if 裡；能決定整個 dfs(i) 的答案 → 才當 base case。
        """
        # 暴力解
        # k = len(s) 
        # def dfs(i: int) -> int:
        #     if i == k:
        #         return 1
        #     if s[i] == "0":
        #         return 0

        #     cur = dfs(i+1)

        #     if (i+1) < k and ((s[i] == "1" and "0" <= s[i+1] <= "9") or
        #      (s[i] == "2" and "0" <= s[i+1] <= "6")):
        #         cur += dfs(i+2)   
            
        #     return cur

        # return dfs(0)

        # 次優解 top down dp
        # k = len(s)
        # dp = [0] * k
        # dp_set = set()
        # def dfs(i: int) -> int:
        #     if i == k:
        #         return 1
        #     if s[i] == "0":
        #         return 0
        #     if i in dp_set:
        #         return dp[i]

        #     dp[i] = dfs(i+1)

        #     if (i+1) < k and ((s[i] == "1" and "0" <= s[i+1] <= "9") or
        #      (s[i] == "2" and "0" <= s[i+1] <= "6")):
        #         dp[i] += dfs(i+2)   

        #     dp_set.add(i)
        #     return dp[i]

        # dp[0] = dfs(0)

        # return dp[0]

        # 次優解 bottom up dp
        # k = len(s)
        # dp = [0] * (k+1)
        # dp[k] = 1

        # for i in range(k-1, -1, -1):
        #     if s[i] == "0":
        #         continue

        #     dp[i] = dp[i+1]

        #     if (i+1) < k and ((s[i] == "1" and "0" <= s[i+1] <= "9") or
        #      (s[i] == "2" and "0" <= s[i+1] <= "6")):
        #         dp[i] += dp[i+2]

        # return dp[0]

        # 最優解 bottom up dp (T:O(n), S:O(1))
        k = len(s)
        
        next1 = 1 # dp[k]
        next2 = 0 # dp[k+1]
        cur = 0
        for i in range(k-1, -1, -1):
            if s[i] == "0":
                cur = 0
            else:
                cur = next1

                if (i+1) < k and ((s[i] == "1" and "0" <= s[i+1] <= "9") or
                (s[i] == "2" and "0" <= s[i+1] <= "6")):
                    cur += next2

            next2 = next1
            next1 = cur
            

        return cur
