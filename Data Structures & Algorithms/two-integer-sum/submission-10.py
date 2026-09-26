class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        * 題目的目標是要找到一個組合符合 nums[i] + nums[j] == target ，而且 i != j 代表組合當中
          不能用重複的 index 而且題目有特別說明，每一個 input 都剛好會有一組解法。然後回傳時比較小
          的 index 放前面。
        * 想法:
            * 有解: 用 hash key 。 先用 for loop 遍歷 nums 所有元素，然後去計算目前元素 (nums[i]) 的
              remain (target - nums[i])， 然後去找這個 remain 是否出現在 dicty 裡面，如果沒有就把目前的
              nums[i] 放到 dicty (dicty[nums[i]] = i)。如果 remain 有，那就是答案，由於這裡只會有一個答案，
              所有就直接回傳。 
            * 沒解: 不可能
        """

        dicty = {}
        res = []

        for i in range(len(nums)):
            remain = target - nums[i]
            # 查
            if remain in dicty:
                return [dicty[remain], i]
            # 維護
            if nums[i] not in dicty:
                dicty[nums[i]] = i

        return []

"""
Two Sum II（全部配對版）

給你一個整數陣列 nums 和一個整數 target，回傳所有滿足 nums[i] + nums[j] == target 的 index pair [i, j]。

每組 pair 必須 i < j（同一個 index 不能用兩次）
不同的 index 組合視為不同答案，即使值相同也要分別輸出
外層 list 的順序不限
沒有任何配對時回傳 []

class Solution:
    def twoSumAll(self, nums: List[int], target: int) -> List[List[int]]:

        dicty  = {}
        
        res = []
        
        for i in range(len(nums)):
            remain = target - nums[i]
            # 查
            if remain in dicty:
                for j in dicty[remain]:
                    res.append([j, i])
            # 維護，讓 dict 去存 0 - i 的 value 與 index
            if nums[i] not in dicty:
                dicty[nums[i]] = [i]
            else:
                dicty[nums[i]].append(i)

        return res

"""