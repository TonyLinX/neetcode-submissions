class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        * 這題的核心是給你一個數字list，去找到 subarray，他的總合最大。這裡期望的 T: O(n) , S: O(1)。
        * 想法:
            * 有解: 就是使用 two point 找到 subarray，當目前的子字串加總還是大於 0 就代表這些總和加總一定會
              更大，只有當目前的加總小於 0，代表該數字不應該加入這個 subarray,因為是負面影響。
            * 無解: 不可能，因為 list 長度一定至少大於 1

        """
        res = float("-inf")

        left  = 0
        temp_sum = float("-inf")

        for right in range(len(nums)):
            if (temp_sum + nums[right]) < nums[right]:
                left = right
                temp_sum = nums[right]
                res = max(res, temp_sum)
            elif nums[right] + temp_sum > 0 :
                temp_sum = temp_sum + nums[right] if temp_sum!=float("-inf") else nums[right]
                res = max(res, temp_sum)
            else:
                left = right + 1
                temp_sum = float("-inf")
    
            
        return res

        