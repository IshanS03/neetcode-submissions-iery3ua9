"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if node:
            copy = Node(1)
            createdNodes = { 1:copy }

            def dfs(copy, node):

                for neighbor in node.neighbors: 

                    if neighbor.val not in createdNodes:
                        new = Node(neighbor.val)
                        createdNodes[neighbor.val] = new 
                        dfs(new, neighbor)         
                    else:
                        new = createdNodes[neighbor.val]

                    copy.neighbors.append(new)
            
            dfs(copy, node)
            return copy
        
        else:
            return
                


        