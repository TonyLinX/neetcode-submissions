class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        @ input: a single string, a number
        @ output: a number
        * 這題是要找到最長的合理的字串，合理的定義是此字串都要同一個字元。
        * 你可以用 k 次 把字串當中的字元進行替換
        * 因為是一個子字串，所以是連續的，這樣跟 sliding window 有點像
        * 當時沒有想到的: 
            * 我能明確想到解題想法，但不知道怎麼實作
            * 這題的重點要找出當下 substring 的長度以及最多的字母數量，想減後是否是小等於 k
            * length - max_count <= k
            * 還有當超過 k 應該是用 while 不斷地將 left 往右靠縮短直到又變成合理
            * 不要用 if , 此時還要維護最多的字母數量
            * max_count = max(count.value()) 這個用法
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

            while length - max_count > k:
                count[s[left]] -= 1
                left += 1
                length = right-left+1
                max_count = max(count.values())

            res = max(res, length)
            right += 1

        return res

            
        
        