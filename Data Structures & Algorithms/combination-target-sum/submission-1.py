class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []

        def dfs(cur_sum: int, cur_path: List[int], start_index: int) -> None:

            nonlocal res, nums, target
            if cur_sum > target:
                return 
            elif cur_sum == target:
                print(cur_sum, target)
                res.append(cur_path.copy())
                return

            for i in range(start_index, len(nums)):
                cur_path.append(nums[i])
                dfs(cur_sum + nums[i], cur_path, i)
                cur_path.pop()
            

        dfs(0, [], 0)
        return res