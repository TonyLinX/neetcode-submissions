class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        * 題目的目標是要找所有三元組合且符合 nums[i] + nums[j] + nums[k] == 0 ，而且 i, j and k 都不同。
          並且組合沒有順序區分，不能重複。
        * 想法:
            * 有解: 多一個 for loop 的 two sum， 讓外層 for loop 去遍歷 nums, 讓每一個元素變成 target，
                    去找他後面的元素所有的 two sum 組合。但是為了避免重複我們必須將每一個組合排序後轉成 tuple 
                    存在 set 裡面。
            * 沒解: 回傳 []
        * 犯錯: 不應該找出每一個元素所有的 two sum 組合，因為這一題是要 value 不是 index。 
                (第 0 個 0, 第 5 個 0) 和 (第 3 個 0, 第 2999 個 0) 在 index 層級是兩組不同的組合，
                但在值層級都是 (0, 0)，對 3Sum 來說是同一個答案。 所以 two sum 應該是用 set 不是 dict
        """
        
        res = []
        pairs_set = set()

        for i in range(len(nums)-1):
            two_sum_all_pairs = self.TwoSum(-nums[i], nums[i+1:])
            if len(two_sum_all_pairs) == 0:
                continue
            for pair in two_sum_all_pairs:
                pair_key = tuple(sorted([nums[i], pair[0], pair[1]]))
                if pair_key not in pairs_set:
                    res.append([nums[i], pair[0], pair[1]])
                    pairs_set.add(pair_key)
        return res

    def TwoSum(self, target: int, nums: List[int]) -> List[List[int]]:
        """
        這裡的 set 主要是被定義成掃到 i 時，seen 記錄 nums[0..i-1] 出現過的值。
        """
        seen = set()
        res = []
        for i in range(len(nums)):
            remain = target - nums[i]

            # 查詢 remain 是否在 set
            if remain in seen:
                    res.append([remain, nums[i]])

            # 維護 set
            if nums[i] not in seen:
                seen.add(nums[i])

        return res
            