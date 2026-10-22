class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        *   這題核心給你一個nums，nums的元素代表從這格最大可以走的步數。那問你說一路這樣走，能不能走到 nums 最
        後一個元素。
        *   想法:
            *   有解:   用 greedy 但不知道為啥使用greedy。
            *   無解: 不可能，頂多不行就回傳False
        * 觀念:
            *   可以使用 greedy 解的 dp，一定可以解， dp 是找到所有可能，並找到答案，greedy 就是每一步都選擇
            最優，最優就可以代表所有的解，而且是最好的解，所以通常 greedy 的複雜度比較低，可以透過限制，來知道
            使用 dp or greedy 。
        """

        fartest = 0

        for i in range(len(nums)):
            if fartest < i:
                break

            fartest = max(fartest, i + nums[i])

        return fartest >= (len(nums)-1)