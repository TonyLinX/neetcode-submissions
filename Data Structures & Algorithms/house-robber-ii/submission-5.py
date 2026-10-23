class Solution:
    def rob(self, nums: List[int]) -> int: 
        """
        *   核心: 跟 House Robber I 一樣，不能搶相鄰的房子，求最多能搶多少。差別是房子排成一圈，頭尾變成鄰居。
        *   想法:
            *   有解: 頭尾不能同時搶，所以最好的搶法一定是「不搶尾」或「不搶頭」其中一種。
                    → 把圓圈切成兩排：nums[0 ~ n-2]（不搶尾）、nums[1 ~ n-1]（不搶頭），
                    各跑一次 House Robber I，取 max。
                *   次優解: dp[i] = 從 head 算起，到第 i 棟最多能搶多少。每棟只有搶或不搶：
                        * 搶：nums[head+i] + dp[i-2]（不能搶前一棟）
                        * 不搶：dp[i-1]
                        => dp[i] = max(nums[head+i] + dp[i-2], dp[i-1])
                        T: O(n)，跑兩次、每棟 O(1)，2n 還是 O(n)。S: O(n)，dp 陣列。
                *   最優解: dp[i] 只用到 dp[i-1]、dp[i-2]，改用兩個變數 prev1、prev2 取代陣列。
                        每棟：cur = max(nums[i] + prev2, prev1)，prev2 = prev1，prev1 = cur。
                        T: O(n)，S: O(1)。
            *   無解: 不存在，至少一間房子。只有一間時頭尾是同一間，直接回傳 nums[0]。
        *   犯錯:
            *   用 head、tail 傳範圍時，nums 的 index 和 dp 的 index 不同：nums[head+i] 對應 dp[i]。
            *   迴圈要從 2 開始，從 0 開始會讀到 dp[-1]、dp[-2]（Python 不報錯，會拿到最後幾格），悄悄算錯。
            *   n == 1 要先處理，否則 house_rob(0, -1) 的 dp 長度是 0，會 index out of range。
        *   Pattern:
            *   一維 DP「選或不選」：只看最後一個位置怎麼處理，取 max。
            *   多出來的限制（圓圈）→ 拆成幾種情況，各自變回已經會的題目。
        """
        # 次優解
        def house_rob(head: int, tail: int):
            k = tail-head + 1
            dp = [0] * k

            if k == 1:
                return nums[head]
            if k == 2:
                return max(nums[head], nums[head+1])

            dp[0] = nums[head]
            dp[1] = max(nums[head], nums[head+1])

            for i in range(2, k):
                dp[i] = max(nums[head+i] + dp[i-2], dp[i-1])


            return dp[k-1]



        n = len(nums)

        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        # 有搶頭沒搶尾 vs 沒搶頭有搶尾
        res = max(house_rob(0, n-2), house_rob(1, n-1))
        
        return res