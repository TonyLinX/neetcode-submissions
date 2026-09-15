class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0
        left, right = 0, len(heights)-1
        
        while left < right:
            result = max(result, min(heights[left], heights[right])*(right-left))
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1


        return result