# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        res = float("-inf")

        def dfs(root: Optional[TreeNode]) -> int:
            nonlocal res
            if root is None:
                return 0

            # 左鍊總和
            left_sum = max(0, dfs(root.left))
            # 右鍊總和
            right_sum = max(0, dfs(root.right))
            res = max(res, root.val + left_sum + right_sum)

            return root.val + max(left_sum, right_sum)
            
        dfs(root)

        return res
        
        