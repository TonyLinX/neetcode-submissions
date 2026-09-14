class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        value_set = set()

        for num in nums:
            if num not in value_set:
                value_set.add(num)
            else:
                return True
        return False
        