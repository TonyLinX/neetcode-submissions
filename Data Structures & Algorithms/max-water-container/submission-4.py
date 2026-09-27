class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        * 這一題的目標是找到最大的 water 容器。然後回傳。
        * 想法:
            * 有解: 使用 tow point 。 left point 是 index 0 ， right point 是 len(heights) - 1，先計算這個組合下的 water container
                    由於我們是要找最大，然後寬會慢慢的縮小，所以縮的那一邊，永遠是最矮的那一邊，因為你縮高的，接下來產生的 conatainer 
                    不會更大。 
            * 沒解: 不可能
        
        """

        left, right = 0, len(heights) - 1
        res = 0
        while left < right:
            curr_container = min(heights[left], heights[right]) * (right-left)
            res = max(res, curr_container)

            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1

        return res