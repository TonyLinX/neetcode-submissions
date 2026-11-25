class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        * 題目核心: 給你兩個字串 s 與 t， 如果兩個是 anagrams 就回傳 true，如果不是就回傳 fasle。
        題目說明，不可能有空字串，最短長度為 1，而且是由小寫字母組成。
        * 想法:
            * 有解: 字謎的定義是，兩個字串，所使用的同樣字母數量都要一樣但順序不管。 所以說我們可以用一個dict，
            去紀錄所有字母的數量，最後遍歷整個dict 的 valus，如果有不等於 0 就回傳 fasle，反之就回傳 true，
            這裡用 dict or array 都可以，只是我想要用 dict。 複雜度: T:O(N), S:O(N)
            * 無解: 不可能。一定有解
        """

        freq = collections.defaultdict(int)

        n = len(s)
        k = len(t)
        
        if n!= k:
            return False

        for i in range(0, n):
            freq[s[i]] = freq.get(s[i], 0) + 1
            freq[t[i]] = freq.get(t[i], 0) - 1
        
        for value in freq.values():
            if value != 0:
                return False
        

        return True

