class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        * 這題核心是給你一個數字陣列以及數字k，k 代表 sliding window 的長度。用這個 sldiing window 在這串數字 list 從左滑到右。
          並回傳每一個 window 裡面最大值組成的 list。
        * 想法:
            * 有解: 
                * 暴力解: 有 n 組 windows ，每一個 windows 都重新掃一遍找到最大值，所以 T: O(n*k); 不須額外的空間所以 S: O(1)。
                * 最優解: 由於暴力解其實會一直重複檢查最大值，導致時間複雜度很高。從第一個 window 跳到下一個 window，其做的事情都是
                        把第一個拿掉加入新的數字。所以這個 window 最大值是否改變就在這裡。當一個新的數字要加入此 window 時，如果
                        他比前面加入的數字還大，那前面那些數字就不用了，所以從尾端一路比較只要比它小就直接從尾端踢掉，直到遇到比他大的。
                        所以最後會變成由大到小的排列，那位什麼比較小孩要保留呢? 原因是，前面的數字會比較早離開，後面比較小的數字可能會變成
                        最大值。 實現方法可以使用雙向佇列，頭一直保持著最大值。當 i >= k-1 的時候，就是把 dequeue 的頭輸出到結果的 
                        list 上，但取 deque 頭當答案之前，先檢查它是否已經離開 window，所以 deque 要存入 index，不是數值，過期就
                        從前端移除。
                        這樣 T: O(n) 因為每一個數字會加入一次 dequeue 跟出去一次這個 dequeue 這樣是 O(2n) ， S: O(k) 因為需
                        要一個 dequeue 去做暫存而且最多只有 k 個。
            * 無解: 不可能，因為 k 一定會小於等於數字 list 的長度。代表 list 一定會有一個東西。
        """
        
        dq = deque()
        res = []

        for i in range(len(nums)):
            # 如果 deque 的尾端數字比新進的數字還小，就踢掉
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            dq.append(i)

            if dq[0] < len(res):
                dq.popleft()

            if i >= (k-1):
                res.append(nums[dq[0]])
        
        return res
            

            

