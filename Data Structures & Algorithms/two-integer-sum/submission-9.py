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
            if remain not in dicty:
                dicty[nums[i]] = i
            else:
                return [dicty[remain], i]

        return []