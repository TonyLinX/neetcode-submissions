class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []    
    
        def helper(path: str, open_count:int, close_count:int ) -> None:
            if open_count + close_count == n*2:
                res.append(path)
                return
                                 
            # 放左括號
            if open_count < n:
                helper(path + "(", open_count + 1, close_count)
            # 放右括號
            if close_count < open_count:
                helper(path + ")", open_count, close_count + 1)

        helper("", 0, 0)

        return res