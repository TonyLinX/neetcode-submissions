class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        * 題目的核心，給你一個不重複的數字 list，回傳所有的可能的子集。注意答案不能有重複且沒有順序要求。
        * 想法:
            * 有解: 找所有排列或組合的題目可以使用遞迴的技巧，那這題要注意不能重複。所以每一次選擇下一個數字，都只能從目前的 index 往後選
            * 無解: 不可能，因為 nums 裡面一定有1個數字，所以一定會是 [[], [n]] 這樣。
        """
        
        res = []
        path = []
        def helper(start: int) -> None:

            res.append(path.copy())

            for i in range(start, len(nums)):
                path.append(nums[i])
                helper(i+1)
                path.pop()
        
        helper(0)

        return res
                