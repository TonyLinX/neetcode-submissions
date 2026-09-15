class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        @ input: a single list
        @ output: 雙層 list
        @ limitation: 一種組合只能出現一次 不管任何順序
        * 找出所有組合可以讓三個數字相加等於0
        * a + b + c = 0 -> b+c = a 所以可以把它變成一種 Two sum
        """
        res = []
        nums.sort()

        left, right = 0, len(nums)-1
        for i, value in enumerate(nums):
            if i == 0 or (i > 0 and value!=nums[i-1]):
                left, right = i + 1, len(nums)-1
                while left < right:
                    if (value + nums[left] + nums[right]) < 0:
                        left += 1
                    elif (value + nums[left] + nums[right]) > 0:
                        right -= 1
                    else:
                        res.append([value, nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left-1]:
                            left += 1
                        while left < right and nums[right] == nums[right+1]:
                            right -= 1
            
        return res