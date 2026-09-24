class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        * 這題目標要找到最長的 substring
        * 技巧可以用 sliding window 因為是找最長的子字串
        * 想法:
            * 暴力解: 檢查每一個字的所有 case， O(n^2) 
            * 最優解: 使用 sliding window 只要字串合法，往右拓寬自寬，紀錄最長的子字串。
                     但是如果不合法了，就沒有必要繼續拓寬，要改成縮短左邊的字串直到合法。
                     合法的字串意思就是不能有重複的字元，如何判斷有沒有字元重複就是使用 set。
        """
        
        res = 0
        left = 0
        char_set = set()

        for i in range(0,len(s)):
            while s[i] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[i])
            res = max(res, i-left+1)
                
        return res
        

    