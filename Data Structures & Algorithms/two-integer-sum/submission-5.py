class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary= {}
        
        for i in range(0, len(nums)):
            remain = target - nums[i]

            if remain not in dictionary:
                dictionary[nums[i]] = i
            else:
                return [dictionary[remain],i]

        return []
        