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
                        *find(x): 找 x 的老大
                        * union(a, b)：找到 a、b 的老大；如果不同 → 讓其中一個老大認另一個當上級（合併），
                        群數 −1；如果相同 → 本來就同一群，不用做。
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

            while node != boss[node]:
                node = boss[node]

            return node

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
