# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        * 這題核心是給你一個 BST以及兩個node，找到他們最深的共同祖先。
        * 想法:
            * 有解:
                * 最優解: 因為剛好是 BST，代表不用去遍歷整棵樹，會剛好只有一條路徑。 走完一條路徑不需要回來走另一條，所以不太需要用遞迴
                        ，可以使用 while loop。 cur 從 root 開始，如果p 與 q 地 val 都比 cur.val 小代表都在左子樹，要繼續往左走。
                        相反都比 cur.val 大，都在右子樹，要繼續往右走。直到當 cur.val 可以分開這兩個 node 或者 cur 目前就等於其中一個 node
                        就是回傳該 node。T: O(h)，只走一條 root 往下的路徑，平衡 O(log n)、歪斜 O(n); S: O(1)，只有一個 cur 變數；用 
                        recursion 寫則是 O(h)。
            * 無解: 不可能，因為整棵樹最少有兩個 node，而且 p and q 一定存在在樹上。

        """
        cur = root
        while cur:
            if p.val < cur.val and q.val < cur.val:
                cur = cur.left
            elif p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif cur == p or cur == q:
                return cur
            else:
                return cur
        
        return cur

        