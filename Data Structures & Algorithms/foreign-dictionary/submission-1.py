class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        """
        * 想法:
            *   有解:   第一步: 先找出所有 edges， for loop 跑所有 words，比較前後找到不同字母得到順序關係
            (edges)，這裡也可能發生一個是另一個得 prefix，如我發現 prefix 在前面->合法，如果在後面->回傳""。
            第二步：所有出現過的字母都建成 node（不能只從 edge 建，否則沒關係的字母會漏掉）；edge a → b 代表 a
            在 b 前面，adj[a] 存排在 a 後面的字母，indegree[b] 存 b 前面還有幾個字母要先放；同一條 edge 可能
            重複，要檢查才加 indegree。第三步：Kahn’s topological sort，indegree 0 的先放，放完通知 adj 裡
            的字母 indegree −1；res 長度小於字母數 → 有環。複雜度（C = 所有單字的字元總數，U = 不重複字母數，
            E = edge 數）：第一步比相鄰單字，每個字元最多比一次 → O(C); 第二步建 node O(C)、加 edge O(E);
            第三步 Kahn’s O(U + E); T: O(C)（U ≤ 26、E ≤ 單字數，都被 C 蓋過）; S: O(U + E)，最多 26 個字
            母，實際上是常數。
            *   無解:   prefix 長的在前、或字母關係有環 → ""
        """

        # first step
        edges = []
        for i in range(len(words)-1):
            str1 = words[i]
            str2 = words[i+1]

            min_len = min(len(str1), len(str2))
            find = False
            for j in range(min_len):
                if str1[j] != str2[j]:
                    find = True
                    edges.append([str1[j], str2[j]])
                    break
            if not find:
                if len(str2) < len(str1):
                    return ""
        
        # second step
        adj = {}
        indegree = {}

        for word in words:
            for c in word:
                adj[c] = set()
                indegree[c] = 0
        
        for a,b in edges:
            if b not in adj[a]: ###### 細節
                adj[a].add(b)
                indegree[b] += 1
        
        # third step (kahn's)
        
        q = deque()

        for key, value in indegree.items(): ##### 遍歷 dict 拿 key and value
            if value == 0:
                q.append(key)

        res = []
        while q:
            top = q.popleft()
            res.append(top)
            for nxt in adj[top]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)
            

        return "" if len(res) < len(indegree) else "".join(res)
        



