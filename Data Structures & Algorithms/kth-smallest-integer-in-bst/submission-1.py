# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        * 這題核心是找到這顆 BST 第 k 個最小的值。
        * 想法:
            * 有解: 
                * 最優解: 可以利用 BST 與 inorder 的特性， 會是一個嚴格遞增的數列。 那用外部參數計數就好。
            * 無解: 不可能，因為 k 一定是比 tree 的node數量還小。
        """
        res = float('inf')
        count = 1
        def dfs(cur: Optional[TreeNode]) -> None:
            nonlocal res, count

            if cur is None or res != float('inf'):
                return None
            
            dfs(cur.left)
            if count == k:
                res = cur.val
            count += 1
            dfs(cur.right)

        dfs(root)
        return res 