class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        * 題目核心: 給你一個 nums 陣列，只要有一個數字出現超過一次就回傳 true。 可能陣列會是空的。
        * 想法:
            * 有解: 用 set 去紀錄所有出現過的數字，只要已經在 set裡面就回傳 true， 如果沒有就加入倒 set，預設
            是回傳 false。 複雜度為 T:O(N), S:O(N)。
            * 無解: 不可能，救回傳 ture or false，但陣列可能為空。
        """

        freq = set()

        for num in nums:
            if num in freq:
                return True
            freq.add(num)

        return False