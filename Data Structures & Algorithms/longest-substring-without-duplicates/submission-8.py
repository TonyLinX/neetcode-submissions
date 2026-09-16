class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letter = set()
        res, count = 0, 0
        left, right = 0, 0

        while right < len(s):
            if s[right] not in letter:
                count += 1
                res = max(res, count)
                letter.add(s[right])
                right += 1
            else:
                while s[right] in letter:
                    letter.remove(s[left])
                    count -= 1
                    left += 1
        return res
            