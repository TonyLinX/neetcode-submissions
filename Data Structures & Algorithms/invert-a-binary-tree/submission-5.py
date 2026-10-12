# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
            * 這題核心是給你一顆 tree 把 root 以下的左子樹與右子樹對調。
            * 想法:
                * 有解: 每一個 TreeNode 都有自己的左子樹與右子樹要進行對調，所以可以使用遞迴。 base case 就是 root node 為 none，
                        遞迴關係就是對調後，呼叫使用左邊的 node 進行遞迴 ， 在呼叫右邊的node進行遞迴。
                * 無解: 不可能，頂多 root 就是 None，剛好 optional 就代表可以回傳 TreeNode or None。
        """

        def dfs(root: Optional[TreeNode]) -> Optional[TreeNode]:
            if root == None:
                return root
        
            temp = root.left
            root.left = root.right
            root.right = temp

            dfs(root.left)
            dfs(root.right)
        
        dfs(root)

        return root