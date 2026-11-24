class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        * 題目核心: 給你一個整數陣列，回傳兩個 index i, j，使得 nums[i] + nums[j] == target，然後 i!= j，且
        每一個 input 一定只有一組解，不可能無解或多個解。
        * 想法:
            * 有解: 
                * 暴力解: 雙迴圈去跑，這樣複雜度為 T:O(N^2),S:O(1)
                * 用 dict 去紀錄每一個數字以及對應的 index，每一個數字只需要判斷 dict[target - nums[i]] 是否
                存在就好了，如果不存在就加入 dict，如果存在就是答案。回傳的時候較小的 index 放前面。複雜度為
                T:O(N),S:O(1)
            * 無解: 不可能，因為題目有說明。
        """


        dictry = dict()
        res = [0,0]
        n = len(nums)
        for i in range(n):
            if target - nums[i] in dictry:
                res = [dictry[target - nums[i]], i]
            dictry[nums[i]] = i
        
        return res