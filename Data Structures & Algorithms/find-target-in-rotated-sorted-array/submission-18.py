class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        這個題目跟上一題一樣，一個有序的陣列被旋轉幾次
        目標是要找到 target
        限制是要在 O(log n)
        """

        left, right = 0, len(nums)-1

        while left <= right:
            mid = (left+right) // 2

            if nums[mid] == target:
                return mid
        
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid -1


        return -1
                