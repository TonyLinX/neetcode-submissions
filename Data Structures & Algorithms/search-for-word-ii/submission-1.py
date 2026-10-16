class TreeNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class PrefixTree:
    def __init__(self):
        self.root = TreeNode()
    def addword(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                node = TreeNode()
                cur.children[c] = node
            cur = cur.children[c]

        cur.is_end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        pt = PrefixTree()
        for word in words:
            pt.addword(word)

        ROW = len(board)
        COL = len(board[0])

        def dfs(cur: TrieNode, row: int, col: int, prefix: str) -> None:
            nonlocal res, ROW, COL

            # 能不能踩這格
            if row < 0 or col < 0 or row >= ROW or col >= COL or board[row][col] == "#":
                return
            if board[row][col] not in cur.children:
                return

            # trie 往下走一步
            temp_char = board[row][col]
            nxt = cur.children[temp_char]

            # 拼出完整 word → 記錄，但不 return
            if nxt.is_end:
                res.append(prefix + temp_char)
                nxt.is_end = False

            # 標記 → 四個方向 → 復原
            board[row][col] = "#"
            dfs(nxt, row - 1, col, prefix + temp_char)
            dfs(nxt, row + 1, col, prefix + temp_char)
            dfs(nxt, row, col - 1, prefix + temp_char)
            dfs(nxt, row, col + 1, prefix + temp_char)
            board[row][col] = temp_char

        for row in range(ROW):
            for col in range(COL):
                dfs(pt.root, row, col, "")

        return res