class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        @ input: a single list
        @ ouput: true or false
        * 判斷是否是回文
        * 整個 string 是由 (A-Z, a-z) and numbers (0-9) 組成
        * 最暴力解法就是複製倒過來
        * 但要先解決空白的部分跟大小寫
        * 大小寫可以透過 str.lower()產生一個全小寫的新 str
        * 空白部分只能一個一個字元檢查
        """
        
        # lower_string = s.lower()
        # clear_string = ""
        # for c in lower_string:
        #     if c.isalnum():
        #         clear_string += c
        
        # reverse_string = clear_string[::-1]

        # 可以寫簡寫成 return clear_string == reverse_string

        # for i in range(len(reverse_string)):
        #     if (reverse_string[i] != clear_string[i]):
        #         return False
        # return True

        # return clear_string == reverse_string



        """
        @ input: a single list
        @ ouput: true or false
        * 判斷是否是回文
        * 整個 string 是由 (A-Z, a-z) and numbers (0-9) 組成
        * 另一種解法不需要任何的額外空間 -> Two points
        * 兩個指針指向左右兩頭。
        * 忽略非英數字元，兩個都是英數字元且相等，否則回傳 False
        """

        left, right = 0, len(s)-1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1

        return True 

