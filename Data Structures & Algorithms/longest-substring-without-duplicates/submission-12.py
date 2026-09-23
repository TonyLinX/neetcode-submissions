class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        * 這題目標要找到最長的 substring
        * 技巧可以用 sliding window 因為是找最長的子字串
        * 想法就是只要字串合法，往右拓寬自寬，紀錄最長的子字串。但是如果不合法了，就沒有必要繼續拓寬，
          要改成縮短左邊的字串直到合法
        """
        count = dict()
        res = 0
        start = 0
        for i in range(0, len(s)):

            count[s[i]] = 1 + count.get(s[i],0)

            while count[s[i]] > 1:
                count[s[start]] -= 1
                start += 1
            
            res = max(res, i-start+1)
            
        return res    

    