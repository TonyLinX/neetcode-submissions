class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1,1,2,8,48]
        # [48,48,24,6,1]
        # i=0: prefix[1] = nums[0] * prefix[0] = 1*1 = 1
        # i=1: prefix[2] = nums[1] * prefix[1] = 2*1 = 2
        # i=2: prefix[3] = nums[2] * prefix[2] = 4*2 = 8
        # i=3: prefix[4] = nums[3] * prefix[3] = 6*8 = 48

        length = len(nums)

        prefix = [1] * (length+1)
        suffix = [1] * (length+1)

        for i in range(0, len(nums)):
            prefix[i+1] = nums[i]*prefix[i]
        
        for i in range(len(nums)-1, -1, -1):
            suffix[i] = suffix[i+1]*nums[i]
        
   

        result = [1]*len(nums)

        for i in range(0, len(nums)):
            result[i] = prefix[i]*suffix[i+1]
        
        return result
