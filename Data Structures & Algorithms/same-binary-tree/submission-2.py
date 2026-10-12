# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
            * 這題核心是給你兩棵樹 root p, root q 判斷這兩棵樹是否一樣。
            * 想法:
                * 有解: 
                    * 最優解: 先用兩個外部參數 list 分別記錄這兩棵樹的結構。 然後用 dfs 遍歷這兩棵樹， base case 為 root is None，
                                回傳 none 。 遞迴關係，把目前 node 放到自己的 list 裡面，然後再遞迴左子樹再遞迴右子樹。
                                兩邊都遍歷完，就比較兩個 list 是否一樣就好了。 
                * 無解: 不可能，頂多不相同回傳 false。
        """


        p_list = []
        q_list = []

        def dfs(root: Optional[TreeNode], lst: List) -> None:

            if root is None:
                lst.append(root)
                return None

            lst.append(root.val)

            dfs(root.left, lst)
            dfs(root.right, lst)
            
        dfs(p, p_list)
        dfs(q, q_list)

        # print(p_list, q_list)

        return p_list == q_list