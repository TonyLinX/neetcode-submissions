# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def dfs(root: Optional[TreeNode]) -> bool:
            if root is None:
                return False
 
            return is_same_tree(root, subRoot) or dfs(root.left) or dfs(root.right)

        def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if p is None and q is None:
                return True
            elif p is None or q is None or p.val != q.val:
                return False
            
            return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

        

        return dfs(root)



    