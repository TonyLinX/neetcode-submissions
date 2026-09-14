class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dicty = dict()

        for i in range(len(strs)):
            count = [0]*26
            
            for c in strs[i]:
                count[ord(c)-ord("a")] += 1
            key = tuple(count)
            
            if key not in dicty:
                dicty[key] = [strs[i]]
            else:
                dicty[key].append(strs[i])
        
        return list(dicty.values())
        