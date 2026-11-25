class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        * 題目: 給你一個 list，裝著多個 string，然後去分類，把字謎的放在同一個 list裡面，然後把所有組的list 都
        放到一個  list 裡面進行回傳。 題目說明一定會給你至少一個字串，但這個字串可能是空字串。
        * 想法:
            * 有解: 我們可以用一個 array 去記錄每一個字串他的組成成分是什麼，比如說 act，就會是 a1b0c1....t1...
            ，cat也會是一樣的，那轉成 tuple 就可以作為key存到某一個 dict，這個 dict 的 vlaue 是字串，
            這樣可以做到分組，最後再便利所有 values， append 到一個 result 的 list裡面回傳。 T: O(N), S:O(N)
            * 無解: 不可能。
        """

        res = []

        group = collections.defaultdict(list)

        for string in strs:
            freq = [0] * 26
            for i in range(0, len(string)):
                freq[ord(string[i]) - ord("a")] += 1
            key = tuple(freq)
            group[key].append(string)
        
        for value in group.values():
            res.append(value)

        return res
            