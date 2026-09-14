class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        map = dict()
        
        for i in range(len(nums)):
            num = nums[i]
            if (target-num) not in map:
                map[num] = i
            else:
                return [map[target-num], i]

        return [] 