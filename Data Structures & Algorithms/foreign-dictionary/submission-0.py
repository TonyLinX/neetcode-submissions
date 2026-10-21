class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        """
        * 想法:
            *   有解:   第一步就是先找出所有 edges， for loop 跑所有 words，比較前後找到不同字母得到順序關係
            (edges)，這裡也可能發生一個是另一個得 prefix，如我發現 prefix 在前面->合法，如果在後面->回傳""。
            第二步
            *   無解:   
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
        



