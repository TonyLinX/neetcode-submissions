class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
            * 這題核心是給你兩個字串 s1, s2，在 s2 中是否能找到一個子字串是 s1 的任意組合。有回傳 true, 沒有回傳 false。
            * 想法: 
                * 有解: 
                    * 暴力解: 找到所有 s1 的所有組合，一個一個去比對是否在 s2 裡面。 這樣花費非常大，光找到組合使用遞迴複雜度就很高。
                    * 最優解: 用 hash map 紀錄 s1 所有字元的數量。將 s2 每一個位置作為開頭。去比對是否有在 s1 的 hash map, 如果中途有一個就重來。
                             只要有一個字元結束就記錄任務完成+1。
                * 無解: 回傳 false
        """
        

        # 次優解 T: O(len(s2) * len(s1))
        # if len(s1) > len(s2):
        #     return False
        
        # s1_char_count = collections.defaultdict(int)

        # for c in s1:
        #     s1_char_count[c] += 1
        
        # all_tasks = len(s1_char_count)

        # for i in range(len(s2)):
        #     s2_char_count = collections.defaultdict(int)
        #     finished_tasks = 0

        #     if (len(s2)-1) - i + 1 < len(s1):
        #         break

        #     for j in range(len(s1)):
        #         s2_char = s2[i+j]
        #         if s2_char not in s1_char_count:
        #             break
        #         s2_char_count[s2_char] += 1
        #         if s2_char_count[s2_char] == s1_char_count[s2_char]:
        #             finished_tasks += 1
                

        #     if finished_tasks == all_tasks:
        #         return True

        # return False


        #  最優解: T: O(len(s2))


        if len(s1) > len(s2):
            return False

        s1_char_count = [0]*26
        s2_char_count = [0]*26

        for c in s1:
            s1_char_count[ord(c)-ord("a")] += 1


        for j in range(len(s1)):
            s2_char = s2[j]
            s2_char_count[ord(s2_char) - ord("a")] += 1

        left, right = 1, 1+len(s1)-1

        while right < len(s2):

            if s1_char_count == s2_char_count:
                return True

            prev_left_char = s2[left-1]
            right_char = s2[right]

            s2_char_count[ord(right_char) - ord("a")] += 1
            s2_char_count[ord(prev_left_char) - ord("a")] -= 1
            
            left += 1
            right += 1

        return s1_char_count == s2_char_count
                    

