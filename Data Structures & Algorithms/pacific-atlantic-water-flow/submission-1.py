class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        *   這題核心是給你一個圖，回傳所有格是可以流向太平洋 (Pacific Ocean) 與 大西洋(Atlantic Ocean)。
        *   想法:
            *   有解: 
                *   暴力解: 把每一個點當作起點，下去判別是否可以走到太平洋與大西洋，如果可以就加入到答案裡。實作方式需要兩個 dfs，
                去檢查是否能找到太平洋或大西洋，判別太平洋是 row or col 是否小於 0，而判別大西洋是 row or col 是否 >= ROW or >= COL。
                在走的情況下我們需要一個 visited set 把走過的 (row, col) 紀錄，要不然會來來回回，導致 recursion error。 假設 row 為 R
                col 為 C，時間複雜度雙層 for loop 走每個 cell 是 O(R*C)，每一個 cell 都要遍歷地圖，最長也就是 O(R*C)，所以是 O((R*C)^2)
                。 那 Space compliexty 也就是 call stack 與 visited O(R*C)
                *   最優解: 反過思考，是從海出發，看能爬到那些格子，就加入到 set，代表這些格子是可以走到某個海洋，最後就取太平洋與大西洋
                set 的交集就是答案。實現方法就是從靠海的格子出發，透過遞迴一路往高的地方走，遇到走過的格子或比上個格子還矮的就回傳。
                時間複雜度，每個點只走過一遍，所以是 O(R*C)。空間複雜度需要 set，為 O(R*C)。
            *   無解: 不可能，因為這張圖一定有一個 cell。
        *   犯錯：一開始用一個 dfs 同時判斷兩個海，下游格子只需要到其中一個海，and / or 都不對 → 要拆成兩個問題分開問
        *   觀念：visited 不用復原，因為「從某格能不能到海」跟走到它的路徑無關；對照 Word Search 要復原，因為同一格在不同路徑代表不同
        位置的字母
        """

        # 暴力解
        # ROW = len(heights)
        # COL = len(heights[0])
        # res = []

        # def dfs_pacific(row: int, col:int, pre_height:int, visited: set) -> bool:
        #     nonlocal ROW, COL, heights

        #     if row < 0 or col < 0:
        #         return True
        #     elif row >= ROW or col >= COL or pre_height < heights[row][col]:
        #         return False
        #     elif (row, col) in visited:
        #         return False
                
        #     visited.add((row,col))

        #     return (dfs_pacific(row, col-1, heights[row][col], visited) or
        #             dfs_pacific(row-1, col, heights[row][col], visited) or
        #             dfs_pacific(row, col+1, heights[row][col], visited) or
        #             dfs_pacific(row+1, col, heights[row][col], visited))
            
        # def dfs_atlantic(row: int, col:int, pre_height:int, visited: set) -> bool:
        #     nonlocal ROW, COL, heights

        #     if row >= ROW or col >= COL:
        #         return True
        #     elif row < 0 or col < 0 or pre_height < heights[row][col]:
        #         return False
        #     elif (row, col) in visited:
        #         return False
                
        #     visited.add((row,col))

        #     return (dfs_atlantic(row, col-1, heights[row][col], visited) or
        #             dfs_atlantic(row-1, col, heights[row][col], visited) or
        #             dfs_atlantic(row, col+1, heights[row][col], visited) or
        #             dfs_atlantic(row+1, col, heights[row][col], visited))

        # for row in range(ROW):
        #     for col in range(COL):
        #         if dfs_pacific(row, col, heights[row][col], set()) and dfs_atlantic(row, col, heights[row][col], set()):
        #             res.append([row,col])

        # return res

        # 最優解
        ROW = len(heights)
        COL = len(heights[0])
        pat, atl = set(), set()
        res = []
        def dfs(row:int, col:int, pre_height:int, ocean_set: set()) -> None:
            if row < 0 or col < 0 or row >= ROW or col >= COL:
                return
            elif pre_height > heights[row][col]:
                return
            elif (row, col) in ocean_set:
                return
        
            ocean_set.add((row, col))

            #上下左右
            dfs(row-1, col, heights[row][col], ocean_set)
            dfs(row+1, col, heights[row][col], ocean_set)
            dfs(row, col-1, heights[row][col], ocean_set)
            dfs(row, col+1, heights[row][col], ocean_set)

        # 最上/最下排
        for col in range(COL):
            dfs(0, col, heights[0][col],pat)
            dfs(ROW-1, col, heights[ROW-1][col],atl)
        
        #最左/右排
        for row in range(ROW):
            dfs(row, 0, heights[row][0], pat)
            dfs(row, COL-1, heights[row][COL-1], atl)

        for row in range(ROW):
            for col in range(COL):
                if (row,col) in pat and (row,col) in atl:
                    res.append([row,col])

        return res
        