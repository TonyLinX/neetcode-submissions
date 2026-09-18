class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        這題是要找出最小值。
        那這種題目通常就是 掃陣列，O(n)就可以解，但題目要求 O(log n)，所以會使用二元搜尋法
        那 二元搜尋法只適用在有排序的陣列。找最小值，又必須要有排序的題目，就會魔改成這樣
        一個 array 有 rotate。 關鍵也就在這裡，你必須判斷 nums[mid]屬於左部分還是右部分
        * 當時的犯錯:
            * 不知道二元搜尋法怎實作
            * while left <= right，是小於等於不只是小於，如果是小於，會在[1,3,5] target= 5 出錯
                i=0, j=2  → m=1, nums[1]=3 < 5 → i = 2
                i=2, j=2  → i < j 不成立,直接跳出 → return -1  ✗ 錯!
        * 這一題深思後的發現:
            * 這一題其實是找斷點在哪邊，假設環狀的陣列，陣列的頭跟尾就是一個不連續的斷點
            * 那最大值與最小值會出現在斷點的左右邊。所以說我用mid去跟 right 判斷是不是連續
            * 如果是連續的就代表斷點在另外一邊，所以要往那邊搜。
            * 使用 res = min(res, nums[mid]) 不是 nums[left] or nums[right] 
                => 因為 left/right 定義我還沒排除的範圍；mid 是我每次實際檢查的點，
                   既用來更新目前看過的最小值，也用來判斷哪一半可以排除。
        """
        left, mid, right = 0, 0, len(nums)-1
        res = float("inf")
        while left <= right:
            mid = (left + right) // 2
            res = min(res, nums[mid])
            # print(left, right, mid , res)
            # mid 屬於右部分
            if nums[mid] <= nums[right]:
                right = mid - 1
            else:
                left = mid + 1
        
        
        return res