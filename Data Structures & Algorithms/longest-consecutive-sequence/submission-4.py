class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        @ input: a single list
        @ output: a number
        @ complexity: O(n)
        * 目標使找出最長的連續序列
        * 連續序列的定義是不管位置找出互相差 1 的遞增序列
        * 因為不用管位置，也不用管數量，只要知道這個數子是否存在就好
        -> 用 set 
        """
        value = set()

        for num in nums:
            value.add(num)
        
        max_length = 0
        
        for num in value:
            count = 0
            # 判斷是否是起點 => 看前面的數字是否存在
            if (num-1) not in value:  
                count = 1
                while 1:
                    num += 1
                    if num not in value:
                        max_length = max(max_length, count)
                        break
                    else:
                        count += 1
        
        return max_length
                    
        