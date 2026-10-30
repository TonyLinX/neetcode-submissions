class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        *   核心: 給一個數字 array，回傳最長嚴格遞增子序列的長度（可以跳著選，不能改順序）。
        *   想法:
            *   有解:
                *   暴力解（遍歷型）: 每個位置當起點，往右只接比自己大的數字，遞迴下去，記錄最長長度。
                    - 複雜度：每次呼叫 dfs 對應一個遞增子序列，子序列由每個數字選或不選決定，最多 2^n 個；
                    每次呼叫跑最多 n 次迴圈 → T: O(n · 2^n)，會 TLE；S: O(n)。
                    - 下一步：改成回傳型 dfs(i) = 以 nums[i] 開頭的最長長度，才能加 memo。
            *   無解: 不存在，至少一個元素，答案最少是 1。
        *   觀念:
            *   遞迴時間 = dfs 被呼叫幾次 × 每次呼叫做的事。
            *   畫樹（分岔數^深度）只在每層分岔差不多時準；這題越往右分岔越少，改數「每次呼叫代表什麼」。
        """
        # 暴力解(遍歷型遞迴)
        # resLen = 1
        # def dfs(i: int, count: int) -> None:
        #     nonlocal resLen
        #     if count > resLen:
        #         resLen = count

        #     for j in range(i+1, len(nums)):
        #         if nums[i] < nums[j]:
        #             dfs(j, count+1)
        
        # for i in range(len(nums)):
        #     dfs(i, 1)

        # return resLen

        # 暴力解(回傳型遞迴)
        """
        *   想法: 可以用 recursion 寫。
            - dfs(i) 定義為 以 nums[i] 開頭的最長遞增子序列長度。
            - base case 後面沒有比 nums[i] 大的數字 → 只有自己 → 回傳 1。
            - recursion 關係下一個數字可以接任何 j > i 且 nums[j] > nums[i] 的位置，
              接上後剩下的就是 dfs(j)，取最長的再加上自己：dfs(i) = 1 + max(dfs(j))。
        """
        # def dfs(i: int)-> int:
        #     LIS = 1
        #     for j in range(i+1, len(nums)):
        #         if nums[j] > nums[i]:
        #             LIS = max(LIS, 1 + dfs(j))
                    
        #     return LIS

        # resLen = 1

        # for i in range(len(nums)):
        #     resLen = max(resLen, dfs(i))

        # return resLen
            
        # dp (Top Down)
        """
        *   想法: 一樣用 recursion寫，只是加入 memo，計算過的就不用算了
            - dp_set 紀錄有計算過的 i
            - dp 定義為 nums[i] 作為開頭，有多長的子序列長度
        """

        dp_set = set()
        dp = [1] *len(nums)
        dp_set.add(len(nums)-1)

        def dfs(i: int)->int :
            if i in dp_set:
                return dp[i]

            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    dp[i] = max(dp[i], 1+dfs(j))

            dp_set.add(i)
            return dp[i]


        res =  1
        for i in range(len(nums)):
            res = max(res, dfs(i))
        
        return res



