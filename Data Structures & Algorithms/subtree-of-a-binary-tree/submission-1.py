# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        res = False
        def dfs(root: Optional[TreeNode]) -> None:
            nonlocal res
            if root is None:
                return None


            if is_same_tree(root, subRoot):
                res = True

            dfs(root.left)
            dfs(root.right)

        def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if p is None and q is None:
                return True
            elif p is None or q is None or p.val != q.val:
                return False
            
            return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

        dfs(root)



        return res



    