class Solution:

    def encode(self, strs: List[str]) -> str:
        encoder_List = []
        for s in strs:
            length = len(s)
            s = str(length) + "#" + s
            encoder_List.append(s)
        
        return "".join(encoder_List)
            
    def decode(self, s: str) -> List[str]:
        
        LIST = []
        i=0
        while i < len(s):
            length = 0
            while 1:
                if s[i] == "#":
                    break
                number = int(s[i])
                i+=1
                length = length*10 + number
            LIST.append(s[i+1:i+1+length])
            i = i + 1 + length
        return LIST

            
