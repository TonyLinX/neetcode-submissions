class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        *   這題核心題目是給你 n 個點以及邊，然後計算有幾個連通區域。
        *   相法:
            *   有解: 
                * 次優解 (標準解): 有給你 n 個點以及 edge，就可以建立成一張圖，然後遍歷所有的點，每一次遍歷就代表這次走過的所有點就算
                是一個連通區域，只要走過就加入 set 裡面，只要被走過就不會再走一次。實作方式，就是先建立 adjacency list (圖)，然後走到一個
                點就往下 dfs 遍歷所有跟他有邊的點。 時間複雜度是，建立圖需要 O(V+E)， 紀錄 visited 為 O(V)， 但 dfs 我不會算 ; 空間複雜
                度需要一個 adjacency list 所以是 O(V+E)。
                * 另解 (Union Find): 複雜度跟 DFS 差不多，但不用建 adjacency list，而且是很多 graph 題的專用工具。
                    *   核心想法: 每一群選一個「老大」一開始每個點自己一群，自己是自己的老大。每讀到一條 edge [a, b]，就把 a 那群和
                    b 那群合併成一群。最後有幾群，就有幾個 component。用 parent list 記錄「我的上級是誰」，一路往上找，找到「上級
                    是自己」的那個就是老大。兩個操作: 
                        * find(x): 找 x 的老大
                        * union(a, b)：找到 a、b 的老大；如果相同就不用作合併，所以回傳 0， 如果不同要做合併→ 根據兩個點的 rank(層數)
                        ，小的作為新的老大，讓另一個合併過來，為甚麼要這樣，原因是避免變成一條 n 長度的 list，這樣每一次 find 很浪費
                        時間，所以才選擇將層數小的合併到層樹高的，這樣層數大的也不會變，層數小的也維持一樣。那只有當層數一樣的時候要將
                        大的層數 + 。 那只要不是相同個父母就需要合併，合併就會少一個群組，所以回傳 1。 這樣時間複雜度是  V 個點 初始化
                        所以是 O(V)， 然後 for loop跑 edge。 加起來就是 O(V+E); 空間複雜度需要兩個 list 為 O(V)。
            *   無解: 不可能，因為是回傳數量。
        """

        # 次優解 (標準解)
        # adj_list = {i:[] for i in range(n)}

        # for a,b in edges:
        #     adj_list[a].append(b)
        #     adj_list[b].append(a)

        # visited = set()
        # res = 0
        
        # def dfs(node: int) -> None:
        #     nonlocal visited
        #     if node in visited:
        #         return

        #     visited.add(node)
        #     for nxt in adj_list[node]:
        #         dfs(nxt)

        # for node in range(n):
            
        #     if node not in visited:
        #         res += 1
        #         dfs(node)

        # return res 

        # Union Find
        boss = [node for node in range(n)]
        rank = [1] * n

        def find(node: int) -> int :
            nonlocal boss

            if node != boss[node]:
                boss[node] = find(boss[node])

            return boss[node]

        def union(n1: int, n2: int) -> int:
            nonlocal boss, rank
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return 0
            elif rank[p1] < rank[p2]:
                boss[p1] = p2
            elif rank[p1] > rank[p2]:
                boss[p2] = p1
            else:
                boss[p1] = p2
                rank[p2] += 1

            return 1

        res = n
        for a, b in edges:
            res -= union(a,b)

        return res
