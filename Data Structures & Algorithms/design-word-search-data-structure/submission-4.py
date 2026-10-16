class TreeNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TreeNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                node = TreeNode()
                cur.children[c] = node
            cur = cur.children[c]
        cur.is_end = True

    def search(self, word: str) -> bool:

        def dfs(cur: TreeNode, i: int) -> bool:
            if i == len(word):
                return cur.is_end
            elif word[i] != "." and word[i] not in cur.children:
                return False 
            elif word[i] == ".":
                for _, child_node in cur.children.items():
                    if (dfs(child_node, i + 1)):
                        return True
                return False
        
            return dfs(cur.children[word[i]], i + 1)
            

        return dfs(self.root, 0)
