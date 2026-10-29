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

        # dpMax = [0]*len(nums)
        # dpMin = [0]*len(nums)
        prevMax, prevMin  = nums[0], nums[0]
        # dpMax[0] = dpMin[0] = nums[0]
        res = float("-inf")
        res = max(prevMax, res)
        
        for i in range(1, len(nums)):
            curMax = max(nums[i], prevMax*nums[i], prevMin*nums[i])
            curMin = min(nums[i], prevMax*nums[i], prevMin*nums[i])
            res = max(curMax, res)

            prevMax = curMax
            prevMin = curMin

        return res
            