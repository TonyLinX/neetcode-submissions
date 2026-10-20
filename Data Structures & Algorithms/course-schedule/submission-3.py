class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        *   這題核心是給你先決條件，按照先決條件下看能不能修完所需修的課程。
        *   想法:
            *   有解: 這題是看到關於有 n 個課程，然後課程之前是有前後關係的，這樣的題目就可以使用到 graph 來建立出彼此的關係。在修每一堂
            課之前，這堂課可能有需要先修的課程。所以要如期完成所有課程是有一個先後順序的。 所以概念是先用 graph 畫出彼此關係，再實際走一遍
            ，如果最後修完的課程不等於所需課程就回傳 false。 實際的作法就是用一個 dict 建立出圖，紀錄每一個課程修完之後會有哪些課程可以修
            ，然後需要一個 list 去記錄目前所有課程還還需要多少先修課，如果等於 0 代表這堂課可以隨時修了。當建立完這些就可以用 bfs 的方式
            逐一遍歷，看最後修完的課程數量是否跟 numCourses 一樣。時間複雜度為 O(n)，空間複雜度也為 O(n)。
            *   無解: 不可能頂多就回傳 false。
        """

        course_map = {}
        for i in range(numCourses):
            course_map[i] = []

        indegree = [0] * numCourses

        # 建立課程地圖與每堂課所需的先修課程數量
        for a, b in prerequisites:
            course_map[b].append(a)
            indegree[a] += 1

        q = deque()

        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)

        count = 0
        while q:
            top = q.popleft()
            count += 1
            for nxt in course_map[top]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)


        return count == numCourses

        
    