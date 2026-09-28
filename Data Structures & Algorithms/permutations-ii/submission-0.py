class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def helper(path: List[int], remain: List[int]) -> None:
            if len(remain) == 0:
                res.append(path)
                return 

            seen = set()

            for i in range(len(remain)):
                if remain[i] in seen:
                    continue
                seen.add(remain[i])
                new_path = path.copy()
                new_path.append(remain[i])
                new_remain = remain[:i] + remain[i+1:]
                helper(new_path, new_remain)

        helper([], nums)

        return res 