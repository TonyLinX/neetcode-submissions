class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
            * 這題的核心是給你一個由小排到大的數字 list，要你回傳一個 indices(1-indexed，從 1 開始) list，他們相加等於 target。只會有一組解，且不能使用
                相同的 index，並且 Space complexity 必定是 O(1)。
            * 想法:
                * 有解: 為了符合空間複雜度的限制，不能使用 hash map。 這一題因為剛好是由小到大，且只有一組解，就可以使 two points， 當左邊的數字加上
                 右邊的數字太小， left + 1，如果太大 right - 1。 這樣複雜度為 T:O(n), S: O(1)。
                * 無解: 不可能，因為題目說一定會有一組解。

        """

        right = len(numbers)-1
        left = 0    

        while left < right:
            temp_sum = numbers[left] + numbers[right] 

            if temp_sum < target:
                left += 1
            elif temp_sum > target:
                right -= 1
            else:
                return [left+1, right+1]
            
