class Solution:
    def rob(self, nums: List[int]) -> int: 

        def house_rob(head: int, tail: int):
            k = tail-head + 1
            dp = [0] * k

            if k == 1:
                return nums[head]
            if k == 2:
                return max(nums[head], nums[head+1])

            dp[0] = nums[head]
            dp[1] = max(nums[head], nums[head+1])

            for i in range(2, k):
                dp[i] = max(nums[head+i] + dp[i-2], dp[i-1])


            return dp[k-1]



        n = len(nums)

        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
            
        # 有搶頭沒搶尾 vs 沒搶頭有搶尾
        res = max(house_rob(0, n-2), house_rob(1, n-1))
        
        return res