class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        n = len(nums)

        total = (0+n) * (n-0+1) // 2

        print(total)

        _sum = 0
        for num in nums:
            _sum += num
        
        return total - _sum