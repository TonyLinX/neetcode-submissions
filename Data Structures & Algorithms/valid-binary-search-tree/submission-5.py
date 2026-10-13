# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        

        def dfs(cur: Optional[TreeNode], low: float, high: float) -> bool:
            if cur is None:
                return True
            elif low >= cur.val  or cur.val >= high:
                return False

            return dfs(cur.left, low, cur.val) and dfs(cur.right, cur.val, high)
        

        return dfs(root, float('-inf'), float('inf'))