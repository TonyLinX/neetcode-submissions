# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
            * 這題核心是給你一顆 tree 把每個 node 的左子樹與右子樹對調。
                * 想法:
                    * 有解: 每個 subtree 也是一棵 tree，翻轉方式一樣 → recursion。
                            base case: node 為 None 就 return。
                            遞迴關係: swap 當前 node 的 left/right，再分別遞迴 left、right。
                            T: O(n)，每個 node 拜訪一次，每次 O(1) swap。
                            S: O(h)，來自 recursion call stack，stack 只存 root 到當前 node 的路徑，最深 = 樹高 h。
                            平衡樹 h = log n → O(log n)；歪斜成一條線 h = n → O(n)。
                    * 無解: 不存在，root 為 None 時直接回傳 None。
        """

        def dfs(root: Optional[TreeNode]) -> None:
            if root == None:
                return None
        
            temp = root.left
            root.left = root.right
            root.right = temp

            dfs(root.left)
            dfs(root.right)
        
        dfs(root)

        return root