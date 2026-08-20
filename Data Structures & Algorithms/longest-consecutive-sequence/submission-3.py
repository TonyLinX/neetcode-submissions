class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        
        result = 0
        for num in num_set:
            # 判斷是否為開頭
            if (num-1) not in num_set:
                count = 1
                while (num+1) in num_set:
                    count+=1
                    num+=1
                result = max(result, count)
        
        return result