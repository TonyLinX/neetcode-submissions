class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        * 這題的目標是要找到所有正確排序的左括右括號的排列。 他是順序有分的，同樣都是 2 個左括號與 2 個右括號，但是 (()) 與 ()() 不同。
        * 想法: 可以用遞回去找，base case 就是左括號加上右括號的數量已達到 2*n。 遞迴關係要如何選擇左括號或右括號。當她要是一個合法的
                左括號與右括號排列的話，左括號要滿足小於n，而右括號的數量最大就是與左括號數量一樣。
        """
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