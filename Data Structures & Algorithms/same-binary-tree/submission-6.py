# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        

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