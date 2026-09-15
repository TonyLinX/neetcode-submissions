class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        @ input: a single list
        @ ouput: a sligle list  
        @ limitation: 必須是 O(n)
        * 這題目的是每一個位置要乘出該位置以外的數字成績，可以將每一個位置分成左邊成績與右邊成績
        * 與運算有關
        * 計算過程高度重複
        => prefix / suffix
        ex.
        [1,2,4,6]
        prefix:[1,1,2,8]
        suffix:[48,24,6,1]
        """
        prefix = [1]*len(nums)
        suffix = [1]*len(nums)

        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1]*nums[i-1]
        
        for i in range(len(nums)-2,-1,-1):
            suffix[i] = suffix[i+1]*nums[i+1]

        result = [1]*len(nums)
        for i in range(len(nums)):
            result[i] = prefix[i]*suffix[i]
        
        return result
