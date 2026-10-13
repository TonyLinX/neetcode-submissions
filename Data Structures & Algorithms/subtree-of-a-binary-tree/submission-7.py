# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        """ 
        * 這題核心是給你兩棵樹 root、subRoot，判斷 root 裡是否有某個 node，以它為根的 subtree 跟 subRoot 完全相同（結構 + 值）。 
        * 想法: 
            * 有解: 
            * 次優解: 外層 DFS 枚舉 root 的每個 node 當候選 root，內層重用 Same Tree 的 is_same_tree 判斷是否跟 subRoot 相同。 
                dfs(node) 回答「以 node 為根的這棵樹裡有沒有包含 subRoot」。 base case: node is None → False（空樹裡找不到，subRoot 
                至少 1 個 node）。 遞迴關係: is_same_tree(node, subRoot) or dfs(node.left) or dfs(node.right)， or 的 short-circuit 
                讓找到之後不會再往下呼叫。 T: O(n·m)，n 個 node 每個都可能做一次最多 O(m) 的比較。 S: O(h1 + h2)，dfs 的 call stack 最深 
                h1，在最深處再疊上 is_same_tree 最多 h2 層；最差 O(n)。 
                * 最優解: Serialization + 字串比對。 把兩棵樹用 preorder + None 標記序列化成字串，subRoot 是 subtree ⇔ subRoot 的字串
                是 root 字串的 substring。 每個值前面要加分隔符（例如 ^12、空寫 #），否則值 2 會被誤判成 12 的一部分。 用 KMP 做 substring 
                比對，T: O(n+m)，S: O(n+m)。 
            * 無解: 不存在，找不到就回傳 False。 
            * 犯錯: 
                * 一開始用 nonlocal res 的遍歷型寫法，找到之後仍會走完整棵樹。改成讓 dfs 回傳 bool，用 or 串左右，自動提早結束。 
                * base case 回傳什麼，取決於函式回答的問題：is_same_tree 兩個都空 → True；dfs 空樹裡找不到 → False。 
                * 如果 subRoot 可能是空的，答案應是 True（空樹是任何樹的 subtree），要在呼叫 dfs 前先處理；本題限制不會出現。 
            * 觀念: 
                * 遍歷型: dfs 回傳 None，結果存外部變數或直接改 tree，適合每個 node 各做各的事（Invert Tree）。 
                * 回傳型: dfs 回傳這棵 subtree 的答案，一路 return 給 parent，適合答案要從 children 組合上來（Same Tree、本題）。 """

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



    