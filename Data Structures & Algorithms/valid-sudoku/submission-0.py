class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # 每列檢查
        for i in range(9):
            temp_set = set()
            for j in range(9):
                if board[i][j] in temp_set:
                    return False
                if board[i][j] != ".":
                    temp_set.add(board[i][j])
        
        # 每行檢查
        for i in range(9):
            temp_set = set()
            for j in range(9):
                if board[j][i] in temp_set:
                    return False
                if board[j][i] != ".":
                    temp_set.add(board[j][i])

        # 列的 9宮格 檢查
        
        for i in range(0,3):
            
            for j in range(0,3):
                
                start_row = 3*i
                start_col = 3*j
                temp_set = set()

                for k in range(3):
                    for l in range(3):
                        if board[start_row+k][start_col+l] in temp_set:
                            return False
                        if board[start_row+k][start_col+l] != ".":
                            temp_set.add(board[start_row+k][start_col+l])


        return True
