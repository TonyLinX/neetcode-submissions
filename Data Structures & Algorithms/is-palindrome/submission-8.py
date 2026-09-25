class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        * 題目的目標是要確定 input s 是否是回文。 是回文就回傳 true 不是就回傳 false。
          回文的定義就是從前面讀跟從後面獨是一樣的，而且不考慮大小寫以及忽略所有非數字或英文字的字元
        * 想法: 可以使用 two point 的技巧。全部先轉成小寫，left point 從左到右， right point 從右到左;
                每一次比對左右邊都要先找到一個是數字或英文字的字元，找到後開始比對，相同就往下繼續找。不相同
                就回傳 fasle
        * special case: 長度一定是 1，如果是 1 就回傳 true
        """
        
        s = s.lower()
        left, right = 0, len(s)-1
        while left < right:
            while left < right and not self.isnumeric(s[left]):
                left += 1
            while left < right and not self.isnumeric(s[right]):
                right -= 1

            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True

    def isnumeric(self, c: str) -> bool:
        if (ord("a") - ord("a")) <= (ord(c) - ord("a")) <= (ord("z") - ord("a")):
            return True
        if (ord("0") - ord("a")) <= (ord(c) - ord("a")) <= (ord("9") - ord("a")):
            return True
        else:
            return False
        