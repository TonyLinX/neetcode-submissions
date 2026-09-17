class Solution:
    def isValid(self, s: str) -> bool:
        """
        這個題目要回傳是否是 valid string
        valid 的判斷就是:
            * 左括號有一個對應相同類型的右括號
            * 左括號會按照正確的順序遇到又括號 -> ([)] 這樣就是有問題的
            * 右括號也會有一個相同類型的對應左括號
        * 當時的犯錯:
            * stack pop 前要判斷 stack 是否有東西
            * return True 之前要判斷 stack 是否都已清空
        """
        stack = []

        for c in s:
            if c in "({[":
                stack.append(c)
            else:
                if len(stack) <= 0:
                    return False
                pop = stack.pop()
                if c == ")" and pop != "(":
                    return False
                elif c == "}" and pop != "{":
                    return False
                elif c == "]" and pop != "[":
                    return False
        
        if len(stack) == 0:
            return True
        else:
            return False
                    
                    