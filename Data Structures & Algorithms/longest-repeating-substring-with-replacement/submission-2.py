class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        @ input: a single string, a number
        @ output: a number
        * 這題是要找到最長的合理的字串，合理的定義是此字串都要同一個字元。
        * 你可以用 k 次 把字串當中的字元進行替換
        * 因為是一個子字串，所以是連續的，這樣跟 sliding window 有點像
        * 當時問題: 我能明確想到解題想法，但不知道怎麼實作
        """
        count = dict()
        left, right = 0, 0
        res = 0
        max_count = 0

        while right < len(s):
            if s[right] not in count:
                count[s[right]] = 1
            else:
                count[s[right]] += 1
            max_count = max(max_count, count[s[right]])
            length = right-left+1
            if left <= right and length - max_count > k:
                count[s[left]] -= 1
                left += 1
                length = right-left+1

            res = max(res, length)
            right += 1
            
        return res

            
        
        