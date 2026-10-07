class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res =  []

        def helper(path: List[int], start: int) -> None:
            if len(path) == k:
                res.append(path)
                return
            
            for i in range(start ,n+1):
                new_path = path.copy()
                new_path.append(i)
                helper(new_path, i+1)

        
        helper([], 1)

        return res