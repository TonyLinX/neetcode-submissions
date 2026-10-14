# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []

        def dfs(root: Optional[TreeNode]) -> None:
            nonlocal res
            if root is None:
                res.append("N")
                return None

            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        
        preorder_index = 0
        # print(data)
        data = data.split(",")
        # print(data)
        def dfs() -> Optional[TreeNode]:
            
            nonlocal preorder_index

            if data[preorder_index] == "N":
                preorder_index += 1
                return None

            root_val = int(data[preorder_index])
            root = TreeNode(root_val)
            preorder_index += 1
            root.left = dfs()
            root.right = dfs()

            return root


        return dfs()



