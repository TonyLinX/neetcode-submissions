class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # tasks = len(t)# !!!!
        
        left, right = 0, 0
        start, end = 0, len(s)-1
        res = float("inf")

        t_map = {}
        s_map = {}
        for c in t:
            t_map[c] = 1 + t_map.get(c, 0)

        tasks = len(t_map)

        while right < len(s):
            char_s = s[right]
            if char_s in t_map:
                s_map[char_s] = 1 + s_map.get(char_s, 0)
                if s_map[char_s] == t_map[char_s]:
                    tasks -= 1
                while tasks == 0:
                    if right-left+1 < res:
                        start, end = left, right
                        res = right-left+1

                    if s[left] in t_map:
                        s_map[s[left]] -= 1
                        if s_map[s[left]] < t_map[s[left]]:
                            tasks += 1
                    left += 1
            right += 1
        if res != float("inf"):
            return s[start:end+1]
        else:
            return ""
                