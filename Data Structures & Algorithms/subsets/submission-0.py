class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        def helper(path: List[int], start: int) -> None:
            if len(path) > len(nums):
                return
            
            res.append(path)

            for i in range(start, len(nums)):
                new_path = path.copy()
                new_path.append(nums[i])
                helper(new_path, i+1)
        
        helper([], 0)

        return res
                