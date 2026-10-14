class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def dfs(row: int, col: int, cur: str) -> bool:
            nonlocal ROW, COL, board, word
            if cur == word:
                return True

            if (row >= ROW or row < 0 or 
                col >= COL or col < 0 or 
                board[row][col] != word[len(cur)] or
                 board[row][col] == "#"):
                return False
            
            cur +=  board[row][col]
            tmp = board[row][col]
            board[row][col] = "#"

            # 上下左右
            found = (dfs(row - 1, col, cur) or
                    dfs(row + 1, col, cur) or
                    dfs(row, col - 1, cur) or
                    dfs(row, col + 1, cur))

            board[row][col] = tmp
            return found

        ROW = len(board)
        COL = len(board[0])

        for i in range(ROW):
            for j in range(COL):
                if dfs(i, j, ""):
                    return True
        
        return False