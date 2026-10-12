# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
            * 這題核心給你一個 tree 的 root，回傳這棵 tree 的高度。
            * 想法:
                * 有解:
                    * 最優解: 用遞迴計算深度，紀錄最大值。 用外部參數紀錄最大值，寫一個遞迴 base case 為 root is None 
                                與外部參數比較目前深度是否為最大值以及回傳 None。遞迴關係用一個參數紀錄目前深度，然後左子樹遞迴
                                並且深度參數+1，回來之後是右子樹遞迴，遞迴下去也是深度參數+1。
                * 無解: 不可能，頂多就是 root 是 none，就回傳 0
        """

        res = 0

        def dfs(depth: int , root: Optional[TreeNode]) -> None:
            nonlocal res
            if root is None:
                res = max(res, depth)
                return None
            
            dfs(depth+1, root.left)
            dfs(depth+1, root.right)
            

        dfs(0, root)

        return res



        