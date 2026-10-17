"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        start = Node(node.val)
        finished = {}
        finished[node] = start
        def dfs(old: Optional['Node'], new: Optional['Node']) -> None:
            nonlocal finished

            for old_neighbor in old.neighbors:
                if old_neighbor not in finished:
                    new_copy = Node(old_neighbor.val)
                    new.neighbors.append(new_copy)
                    finished[old_neighbor] = new_copy
                    dfs(old_neighbor, new_copy)
                else:
                    new.neighbors.append(finished[old_neighbor])
                

        dfs(node, start)

        return start