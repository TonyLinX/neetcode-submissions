class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0
        left, right = 0, len(heights)-1
        
        while left < right:
            result = max(result, min(heights[left], heights[right])*(right-left))
            if (left+1) < right:
                result = max(result, min(heights[left+1], heights[right])*(right-(left+1)))
            if left < (right-1):
                result = max(result, min(heights[left], heights[right-1])*((right-1)-left))

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1


        return result