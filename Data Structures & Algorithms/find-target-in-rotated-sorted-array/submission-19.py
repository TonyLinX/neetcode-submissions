class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        這個題目跟上一題一樣，一個有序的陣列被旋轉幾次
        目標是要找到 target
        限制是要在 O(log n)
        * 當時的犯錯:
            * 邏輯錯誤:
                * 找出有序的那一半
                * 問：target 在這一半的範圍裡嗎？
                * 在 → 搜這一半；不在 → 搜另一半
            * 不知道等號怎麼放，跟放哪裡。
            * mid = (left+right) // 2， mid 都是偏左(當數量<=2)，所以 nums[left] <= nums[mid]，需要等號
            * 而 right 不需要。
            * nums[left] <= target < nums[mid] or nums[mid] < target <= nums[right] 的等號
              是為了檢察 target 是不是剛好在左半邊或右半邊。 例如: [3,1] target = 1
        """

        left, right = 0, len(nums)-1

        while left <= right:
            mid = (left+right) // 2

            if nums[mid] == target:
                return mid

            # 左邊有序
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # 右邊有序
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid -1


        return -1
                