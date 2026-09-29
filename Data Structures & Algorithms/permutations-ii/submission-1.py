class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
        跟 46 題很像，只是說他多了一個 seen，目的是判斷在相同 path 下是不是正要處裡的 reamin 這個值已經處裡過了。如果之前處裡過了
        那就剪枝 
        """
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