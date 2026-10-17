class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        ROW = len(grid)
        COL = len(grid[0])

        def dfs(row: int, col:int) -> None:
            nonlocal grid
            if row < 0 or col < 0 or row >= ROW or col >= COL or grid[row][col] == "0":
                return
            elif grid[row][col] == "#":
                return
            
            grid[row][col] = "#"

            # 上下左右
            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row, col + 1)

            return None

        for row in range(ROW):
            for col in range(COL):
                if grid[row][col] == "1":
                    count += 1
                    dfs(row, col)

        return count