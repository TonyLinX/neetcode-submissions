# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        * 這題核心給你兩個 list，分別為inorder與 preorder，然後建立一棵樹。
        * 想法:
            * 有解: 
                * 次優解: 建立樹可以用遞迴來寫，因為每一個點都可能是 root，所以都要遍歷下去。
                            所以可以用 dfs 完成，利用 preoder 找出 root，再用 inorder 區
                            分左右。實現方式就是 preorder 的第一個點都是 root，用這個 root
                            去 inorder 找到該 index，就會代表前面有mid個左子樹，那index後面
                            就都是右子樹，那為了遞迴下去繼續建立樹，也要重新找出下一個點的
                            preorder與inorder。 由於有n個點，每個點都要去做 inorder.index
                            的 O(n) 操作以及 slice O(n) 操作，這樣是 T:O(n^2); 因為每個點
                            都會有新的 list，這些 list 最差(歪斜樹)差會是 O(n^2)
                * 最優解: 優化 inorder.index 的 O(n)操作，不要每一個 node 重新做一次，而是
                        前面用一個 map 去紀錄，這樣每一個 node 查詢就是 O(1)， n個點就是 O(n)
                        ; 另一方面，改傳 left, right 來得到左子樹或右子樹的範圍。
            * 無解: 不可能，因為這棵樹確實已經存在，只是需要 rebuild。
        """
        # 次優解
        # if preorder == []:
        #     return None
        # root = TreeNode(preorder[0])
        # mid = inorder.index(preorder[0])# 回傳的 index 就可以知道左子樹有幾個
        # # 左子樹
        # new_left_inorder = inorder[:mid]
        # new_left_preorder = preorder[1:mid+1]

        # # 右子樹
        # new_right_inorder = inorder[mid+1:]
        # new_right_preorder = preorder[mid+1:]

        # root.left = self.buildTree(new_left_preorder, new_left_inorder)
        # root.right = self.buildTree(new_right_preorder, new_right_inorder)
        

        # return root

        # 最優解
        inorder_index = {}
        for i in range(len(inorder)):
            inorder_index[inorder[i]] = i

        preorder_index = 0

        def dfs(left, right) -> Optional[TreeNode]:
            nonlocal inorder_index, preorder_index
            if left > right:
                return None
            
            root = TreeNode(preorder[preorder_index])
            mid = inorder_index[preorder[preorder_index]]
            preorder_index += 1
            root.left = dfs(left, mid-1)
            root.right = dfs(mid+1, right)

            
            return root

        return dfs(0, len(inorder)-1)
        