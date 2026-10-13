# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
            * 這題核心是給你兩棵樹 root p, root q 判斷這兩棵樹是否一樣（結構相同且每個對應 node 的值相同）。
            * 想法:
                * 有解:
                    * 次優解: 用兩個外部 list 分別記錄兩棵樹的 preorder 序列，再比較兩個 list 是否相同。
                                base case: root is None 時 append None 當空標記（沒有標記的話 [1,2] 和 [1,null,2] 會被當成一樣）。
                                遞迴關係: append 當前 node 的 val，再遞迴左子樹、右子樹。
                                T: O(n+m)，兩棵樹都要完整走完；S: O(n+m)，兩個 list 存所有 node 和空標記。
                    * 最優解: 同時遞迴兩棵樹，邊走邊比（preorder：先比當前 node，再遞迴左右）。
                        * 兩個都是 None → True
                        * 只有一個是 None，或 val 不同 → False
                        * 都不為空且 val 相同 → 遞迴比較 (左, 左) and (右, 右)
                      T: O(min(n, m))，遇到不同就停（and 的 short-circuit），兩棵完全相同時最差 O(n)。
                      S: O(h)，只有 recursion call stack，h 為樹高；平衡樹 O(log n)，歪斜樹 O(n)。
                * 無解: 不存在，不相同就回傳 False。
            * 犯錯:
                * 非 None 時不能 append root，要 append root.val。TreeNode 物件的 == 預設比的是「是不是同一個物件」，
                    p 和 q 的 node 是不同物件，即使 val 一樣也會判定不同。
                * 空標記不能用 -999 這類數字，會跟合法的 node 值撞（值範圍 -10^4 ~ 10^4），要用 None。
                * 判斷順序要先檢查 None 再讀 .val，靠 short-circuit 避免對 None 取 .val。
                * list 可以同時放不同型別的東西（例如 int 和 None）。
        """

        #  次憂解
        # p_list = []
        # q_list = []

        # def dfs(root: Optional[TreeNode], lst: List) -> None:

        #     if root is None:
        #         lst.append(root)
        #         return None

        #     lst.append(root.val)

        #     dfs(root.left, lst)
        #     dfs(root.right, lst)
            
        # dfs(p, p_list)
        # dfs(q, q_list)

        # return p_list == q_list

        
        # 最優解:
        
        def dfs(p: Optional[TreeNode], q:Optional[TreeNode]) -> bool :
            if p is None and q is None:
                return True
            elif p is None or q is None or q.val != p.val:
                return False

            return dfs(p.left, q.left) and dfs(p.right, q.right)
        
        return dfs(p,q)