class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}

        for string in strs:
            count=[0]*26
            for c in string:
                count[ord(c)-ord("a")]+=1
            key = tuple(count)

            if key not in dictionary:
                dictionary[key] = [string]
            else:
                dictionary[key].append(string)
        
        return list(dictionary.values())