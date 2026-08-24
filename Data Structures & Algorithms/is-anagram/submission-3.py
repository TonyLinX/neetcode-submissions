class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        count = [0]*26

        for cs, ct in zip(s, t):
            count[ord(cs)-ord("a")]+=1
            count[ord(ct)-ord("a")]-=1
        
        for num in count:
            if num != 0:
                return False

        return True