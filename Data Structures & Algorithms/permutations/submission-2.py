class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        * 這題的目標就是要找到所有排列 (permutation)， permutation 是有順序區分的，不像組合 (combination)。
        * 想法: 找到所有排列就可以使用遞迴的方式，那這題沒有重複的元素所以不用處理重複。總共 list 有 i 個元素，找到所有組合的方式就是
                按著 for loop 把每一個元素放到第 i 個位置，可以用樹的方式表達，每一個節點就是選擇的結果，每個結果都會有當下的 path 以及
                remain，當還沒有到達 base case 就一直選，直到 reamin 已經沒有元素的時候就代表，到樹的葉節點，那就是一種排列，把排列加入
                到 res，然後回到上一層。
        """
        res = []
        
        def helper(path: List[int], remain: List[int]) -> None:
            if len(remain) == 0:
                res.append(path)
                return 
            
            for i in range(len(remain)):
                new_path = path.copy()
                new_path.append(remain[i])
                new_remain = remain[:i] + remain[i+1:]
                helper(new_path, new_remain)

        helper([], nums)

        return res 