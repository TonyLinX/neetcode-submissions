class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        * input 為一個由 uppercase 組成的字串。 給你 k 次轉換字元的機會。
           回傳最長的 substring 且只能是一個字元組成。
        * 想法: 紀錄目前字串長度多少以及最多的那個字元有幾個，目前字串長度減掉最多的那個字元數量，
                就代表有多少其他的字元，如果說是 <= K 代表這都是合法字串。如果大於 K 代表不合法。
                就要從左邊縮小字串，然後計算字串長度以及最多的那個字元是多少，一樣互相減是不是合法
                如果尚未合法那就要繼續縮。 這樣的寫法可以用 sliding window 的技巧。
                複雜度為 T: O(n^2) S: O(n)
                
        """

        res = -1
        left = 0
        count = {}

        for i in range(0, len(s)):
            count[s[i]] = 1 + count.get(s[i], 0)
            curr_len = i - left + 1
            max_char_count = max(count.values())
            other_char_count = curr_len - max_char_count
            
            while other_char_count > k:
                count[s[left]] -= 1
                left += 1
                curr_len = i - left + 1
                max_char_count = max(count.values())
                other_char_count = curr_len - max_char_count

            res = max(res, i - left + 1)
        
        return res
            