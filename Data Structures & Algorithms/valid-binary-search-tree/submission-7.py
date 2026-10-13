# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
            * 這題核心是確認這棵樹是否是 BST。
            * 想法:
                * 有解: 
                    * 最優解: 這是一種 top down 的方式，而且top down 通常就是 preorder，因為先處裡自己才去遞迴到 childern 。
                            因為要回來遍歷整棵樹，可以使用遞迴。檢查方式就是確認一個 node 的左子樹是否是都小於他以及他的右子樹是否都大於他，
                            題目有說不能是等於。實現方式就是用 low 與 high 作為這個 node 的範圍。 base case 是 cur node is none，就回傳
                            true，因為他沒有違反。只要違反就回傳 false。遞迴關係為先遞迴左子樹再遞迴右子樹，整棵樹只要沒有任何一個 fasle 
                            就是 BST。因為每一個 node 都要遍歷，每一個 node 只要做 O(1) 的操作，所以 T: O(n); 不需要額外參數，
                            只有 call stack，所以 S: O(h)，最差就是  O(n)。
                    * 另種解法: 這是一種 BST 的 inorder， 可以藉由 BST 的特性：inorder 走出來的值一定嚴格遞增。 inorder 就是左子樹先走完才
                                處裡自己。實現方式就是 dfs 進行 inorder， base case 是 cur is none return True，然後先遞迴左子樹，回來才去
                                多用一個外部額外參數，去紀錄前一個 node 的 val，去跟 cur node 比較較，如果不是遞增就回傳 False，如果不違反，
                                就先更新此外部參數並繼續遞迴右子樹。 這個寫法 T: O(n), S: O(h)
                * 無解: 不可能，因為 root 不可能為 none，所以就是回傳 true or false 。
        """
        # TOP-DOWN
        # def dfs(cur: Optional[TreeNode], low: float, high: float) -> bool:
        #     if cur is None:
        #         return True
        #     elif low >= cur.val  or cur.val >= high:
        #         return False

        #     return dfs(cur.left, low, cur.val) and dfs(cur.right, cur.val, high)
        
        # return dfs(root, float('-inf'), float('inf'))

        # BST+Inorder
        prev = float('-inf')
        def dfs(cur: Optional[TreeNode]) -> bool:
            nonlocal prev
            if cur is None:
                return True
            
            if not dfs(cur.left):
                return False
            
            if prev >= cur.val:
                return False
            
            prev = cur.val

            return dfs(cur.right)



        return dfs(root)
