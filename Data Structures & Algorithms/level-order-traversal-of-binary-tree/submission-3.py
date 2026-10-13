# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
            * 核心: 一層一層由左到右讀出 node 值，每層一個 list，回傳 List[List[int]]。
            * 想法:
                * 有解:
                    * 最優解: BFS（loop + queue）。queue 放入 root，當 queue 不為空:
                                k = len(q) 固定這層 node 數 → 跑 k 次 popleft，收 val，非空 children append 進 queue → 這層 list 加進 res。
                                T: O(n)，每個 node 進出 queue 各一次。S: O(w)，w 為最寬層，最差 O(n)。
                * 無解: root 為 None → 回傳 []（不是 [[]]）。
            * 犯錯:
                * deque() 要加括號；拿頭用 popleft()，deque 沒有 top。
                * append children 前要檢查 None，否則下一輪讀 None.val 報錯。
            * 觀念:
                * Queue FIFO → BFS；Stack LIFO → DFS。popleft 保證上一層先處理完，改 pop() 就變 DFS。
                * BFS 吃寬度 O(w)，DFS 吃深度 O(h)。
        """
        if root is None:
            return []

        q = collections.deque()
        q.append(root)
        res = []
        while q:
            temp = []
            k = len(q)
            for i in range(k):
                node = q.popleft()
                temp.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            res.append(temp)
        return res