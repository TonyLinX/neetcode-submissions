class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        isDuplicate = set()

        for num in nums:
            if num in isDuplicate:
                return True
            else:
                isDuplicate.add(num)
        
        return False