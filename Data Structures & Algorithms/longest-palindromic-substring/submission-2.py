class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        res_len = 0
        k = len(s)
        for i in range(len(s)):
            left, right = i, i

            # 檢查奇數
            
            while left >= 0 and right < len(s) and s[left] == s[right]:
                length = right - left + 1
                if length > res_len:
                    res_len = length
                    res = s[left : right+1]
                left -= 1
                right += 1

            left, right = i, i+1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                length = right - left + 1
                if length > res_len:
                    res_len = length
                    res = s[left : right+1]
                left -= 1
                right += 1

            

        return res