class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        *   這題核心是要確認這個 node 數量與 edge 組成的是一個合法的樹。確認合法的樹就是判斷是否有環以及是否有孤島。
        *   想法:
            *   有解: 所以說判斷是否是 valid tree ，目標就是要判斷是否有環或孤島。判斷這兩個可以分成兩步驟，第一步驟就是透過edge
            數量去判斷，一棵 valid tree 有個 n 個點就一定是 n-1 條 edge，多一條可能有環，少一條可能有孤島。 但是 n-1條邊的情況
            下還是有 invalid tree，所以需要第二步驟去看是否能連通所有點，如果可以就代表就是 valid tree，如果不是就代表有孤島以及環。
            實作方式，先判斷 n-1 條 edge ; 
            *   無解: 不可能，頂多就是回傳 false
        """


        if len(edges) != (n-1):
            return False

        # 建立圖 (adjacency list)
        adj_map = {i:[] for i in range(n)}

        # 把關係建立到圖裡
        for a,b in edges:
            adj_map[a].append(b)
            adj_map[b].append(a)

        count = 0
        visited = set()

        def dfs(node: int) -> None:
            nonlocal count, visited
            if node in visited:
                return 
            count += 1
            visited.add(node)

            for nxt in adj_map[node]:
                dfs(nxt)

            return
        
        dfs(0)

        return count == n