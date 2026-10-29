class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        # res = float("-inf")
        # for i in range(len(nums)):
        #     cur = nums[i]
        #     res = max(cur, res)
        #     for j in range(i+1, len(nums)):
        #         cur *= nums[j]
        #         res = max(res, cur)

        # return res

        # 最優解(dp)

        dpMax = [0]*len(nums)
        dpMin = [0]*len(nums)
        dpMax[0] = dpMin[0] = nums[0]
        res = float("-inf")
        for i in range(1, len(nums)):
            
            dpMax[i] = max(nums[i], dpMax[i-1]*nums[i], dpMin[i-1]*nums[i])
            dpMin[i] = min(nums[i], dpMax[i-1]*nums[i], dpMin[i-1]*nums[i])
            res = max(dpMax[i], res)

        return res if len(nums) > 1 else nums[0]
            