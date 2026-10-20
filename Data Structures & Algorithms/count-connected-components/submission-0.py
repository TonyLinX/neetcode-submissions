class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        

        adj_list = {i:[] for i in range(n)}

        for a,b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)

        visited = set()
        res = 0
        
        def dfs(node: int) -> None:
            nonlocal visited
            if node in visited:
                return

            visited.add(node)
            for nxt in adj_list[node]:
                dfs(nxt)

    
        for node in range(n):
            
            if node not in visited:
                res += 1
                dfs(node)


        return res 

        