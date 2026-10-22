class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
*   核心: nums[i] 代表在第 i 格最多能跳幾格。從 index 0 出發，問能不能走到最後一格。
*   想法:
    *   暴力解(DP): 用一個 list reach 記每一格到不到得了。從左到右，到得了的格子就把它能跳到的格子都標成 True。
                T: O(n²)，S: O(n)。n 最大 10^4，O(n²) 約 10^8，Python 可能 TLE。
    *   最優解(Greedy): 用手玩一次會發現，腦中只需要記一個數字：farthest（目前最遠能到哪）。
                因為 nums[i] 是「最多」跳幾格，最遠能到 6，代表 0 ~ 6 全部都到得了，不用記每一格。
                從左到右走每一格 i：
                    i > farthest → 這格到不了，break
                    否則 farthest = max(farthest, i + nums[i])，看從這格起跳能不能更遠
                最後 farthest >= len(nums) - 1 → True。
                T: O(n)，只掃一次。S: O(1)，只用一個變數。
    *   無解: 走到某一格 i > farthest（被 0 卡住，前面都跳不過）→ False。
*   觀念:
    *   Greedy（貪心）: 每一步都直接拿眼前最好的，不考慮以後、不回頭。這題的 max(...) 就是貪心：
        永遠只留最遠的距離，比較近的直接丟掉。
    *   判斷會不會吃虧：問「我丟掉的東西，以後會不會用到？」
        這題丟掉比較近的距離，但最遠能到的範圍已經包含它們 → 不會吃虧 → 可以用 greedy。
        反例：硬幣 1、3、4 找 6，貪心拿 4 + 1 + 1 = 3 枚，但 3 + 3 只要 2 枚 → 會吃虧 → 要用 DP。
    *   錯的貪法：每次都跳最遠，[2,5,0,0,0] 會跳到 0 卡住。對的貪法是每一格都看過，只記整體最遠。
    *   流程: 先想一定對的解(DP) → 看 constraints 夠不夠快 → 太慢就找能不能只記一個數字(greedy)。
*   犯錯:
    *   變數名 fartest → farthest。
"""

        fartest = 0

        for i in range(len(nums)):
            if fartest < i:
                break

            fartest = max(fartest, i + nums[i])

        return fartest >= (len(nums)-1)