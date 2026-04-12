"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None


        hs = {}
        start = node
        stack = [start]; visited = set([start])

        while stack:
            node = stack.pop()
            hs[node] = Node(val = node.val)
        
            for ele in node.neighbors:
                if ele not in visited:
                    visited.add(ele)
                    stack.append(ele)
        
        for old, new in hs.items():
            for nei in old.neighbors:
                new_ = hs[nei]
                new.neighbors.append(new_)
        
        return hs[start]













