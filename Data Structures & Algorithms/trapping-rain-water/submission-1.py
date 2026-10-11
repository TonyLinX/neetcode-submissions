class Solution:
    def trap(self, height: List[int]) -> int:
        
        res = 0
        #  暴力解
        # for i in range(len(height)):
        #     left = i-1
        #     left_max = 0
        #     while left >= 0:
        #         left_max = max(left_max, height[left])
        #         left -= 1

        #     right = i+1
        #     right_max = 0
        #     while right < len(height):
        #         right_max = max(right_max, height[right])
        #         right += 1
            
        #     water = max(0, min(left_max, right_max) - height[i])
        #     res += water
        #

        # 最優解
        left_max_list = [0]* len(height)
        right_max_list = [0]* len(height)

        for i in range(1, len(height)):
            left_max_list[i] = max(left_max_list[i-1], height[i-1])

        for i in range(len(height)-2,0,-1):
            right_max_list[i] = max(right_max_list[i+1], height[i+1])

        for i in range(len(height)):
            water = max(0, min(left_max_list[i], right_max_list[i]) - height[i])
            res += water
        return res
