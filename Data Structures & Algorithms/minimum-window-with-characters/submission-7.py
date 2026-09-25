class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        * 題目的目標是在 s 中找到一最短的子字串，這個子字串要涵蓋所有 t 的字元，包含重複項。
        * 想法: 找到子字串可以使用 sliding window。 就是先一直往右擴，擴到找到所有 t 的字元，才開始從左邊縮
                找到最短的子字串但還是合法的。
                合法判斷: 紀錄 t 字元種類有幾個且個別是幾個，這樣作為一個任務，當所有任務都達標，才是合法。
                往內縮的時候就是要開始判斷是否還是合法，不合法就不用縮繼續往右擴直到合法。
        * 犯錯: (if char_s_count_map[s[i]] == char_t_count_map[s[i]]) 不應該這樣寫因為 s 某些字元是不會在
                char_t_count_map[s[i]] 裡面出現
        """

        char_t_count_map = {}
        for char_t in t:
            char_t_count_map[char_t] = 1 + char_t_count_map.get(char_t, 0)

        tasks = len(char_t_count_map)
        left = 0
        char_s_count_map = {}
        finish_tasks = 0
        
        res_left, res_rihgt, shortest_len = 0, 0, float("INF")
        for i in range(0, len(s)):

            char_s_count_map[s[i]] = 1 + char_s_count_map.get(s[i], 0)
            if (s[i] in char_t_count_map) and char_s_count_map[s[i]] == char_t_count_map[s[i]]:
                finish_tasks += 1

            while finish_tasks >= tasks:
                char_left = s[left]
                curren_len = i - left + 1

                if curren_len < shortest_len:
                    res_left, res_right, shortest_len = left, i , curren_len

                char_s_count_map[char_left] -= 1
                left += 1

                if (char_left in char_t_count_map) and char_s_count_map[char_left] < char_t_count_map[char_left]:
                    finish_tasks -= 1
        
        return s[res_left:res_right+1] if shortest_len != float("INF") else ""

