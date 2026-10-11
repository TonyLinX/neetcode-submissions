class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        * 這個題目的核心是要去判斷是否是合法的數獨地圖，所以要檢查三個條件，每個 col or 每個 row or 每個九宮格，不能有重複的。
        * 想法:
            * 有解: 
                * 最優解: 想法就是 每 row, 每 col, 每個 9 宮格都創建一個 set。 去紀錄是否有重複值，如果有重複就回傳 false。 那這裡可以使用
                 defaultdict(set)，因為當沒有這個 key 他就會自己創建這個 key 以及 value 預設為 空 set。 走遍數獨地圖上每一格，然後去比對
                 他所在的 row set 與 col set 還有九宮格，是否有重複。如果有重複就回傳 False。到最後都沒有違反就回傳 true。 這題不是一個無限
                 大的數獨地圖，是 9*9 地圖，所以 T: O(1), S: O(1)。 
            * 無解: 無解回傳 False
        """

        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == ".":
                    continue
                if (board[i][j] in rows[i] or
                    board[i][j] in cols[j] or
                    board[i][j] in squares[(i//3, j//3)]):
                    return False

                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                squares[(i//3, j//3)].add(board[i][j])

        return True
