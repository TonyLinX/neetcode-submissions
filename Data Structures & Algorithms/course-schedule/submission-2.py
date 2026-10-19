class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # 先建立好每門課的圖
        adj = {}
        for i in range(numCourses):
            adj[i] = []

        # adj = {
        #     0: [1],      # 修完 0，解鎖 1
        #     1: [2, 3],   # 修完 1，解鎖 2、3
        #     2: [],       # 修完 2，沒有解鎖別的
        #     3: [],
        # }

        # 記錄每門課還差幾門（indegree）
        indegree = [0] * numCourses     # [0, 0, 0, 0]

        # 把每個先決條件放進去
        for a, b in prerequisites:
            adj[b].append(a)
            indegree[a] += 1 

        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
            
        count = 0

        while q:
            top = q.popleft()
            count += 1
            
            for nxt in adj[top]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)

        return count == numCourses