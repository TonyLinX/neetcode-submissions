class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        temp = [0]*26

        # 直接用字元的寫法
        # for char_s, char_t in zip(s,t):
        #     temp[ord(char_s) - ord("a")] += 1
        #     temp[ord(char_t) - ord("a")] -= 1
        
        # 用索引的寫法
        for i,j in zip(range(len(s)), range(len(t))):
            temp[ord(s[i]) - ord("a")] += 1
            temp[ord(t[j]) - ord("a")] -= 1
        
        for num in temp:
            if num != 0:
                return False
        
        return True