class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        *   這題核心是給你一個圖，回傳所有格是可以流向太平洋 (Pacific Ocean) 與 大西洋(Atlantic Ocean)。
        *   想法:
            *   有解: 
                *   次優解: 把每一個點當作起點，下去判別是否可以走到太平洋與大西洋，如果可以就加入到答案裡。
            *   無解: 不可能，因為這張圖一定有一個 cell。
        """

        ROW = len(heights)
        COL = len(heights[0])
        res = []

        def dfs_pacific(row: int, col:int, pre_height:int, visited: set) -> bool:
            nonlocal ROW, COL, heights

            if row < 0 or col < 0:
                return True
            elif row >= ROW or col >= COL or pre_height < heights[row][col]:
                return False
            elif (row, col) in visited:
                return False
                
            visited.add((row,col))

            return (dfs_pacific(row, col-1, heights[row][col], visited) or
                    dfs_pacific(row-1, col, heights[row][col], visited) or
                    dfs_pacific(row, col+1, heights[row][col], visited) or
                    dfs_pacific(row+1, col, heights[row][col], visited))
            
        def dfs_atlantic(row: int, col:int, pre_height:int, visited: set) -> bool:
            nonlocal ROW, COL, heights

            if row >= ROW or col >= COL:
                return True
            elif row < 0 or col < 0 or pre_height < heights[row][col]:
                return False
            elif (row, col) in visited:
                return False
                
            visited.add((row,col))

            return (dfs_atlantic(row, col-1, heights[row][col], visited) or
                    dfs_atlantic(row-1, col, heights[row][col], visited) or
                    dfs_atlantic(row, col+1, heights[row][col], visited) or
                    dfs_atlantic(row+1, col, heights[row][col], visited))

        for row in range(ROW):
            for col in range(COL):
                if dfs_pacific(row, col, heights[row][col], set()) and dfs_atlantic(row, col, heights[row][col], set()):
                    res.append([row,col])

        return res    