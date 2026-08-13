# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        max_diameter = 0
        heights = {}  # Store height of each node
        stack = [(root, False)]  # (node, children_processed)
        
        while stack:
            node, children_processed = stack.pop()
            
            if children_processed:
                # Post-order: process after children are done
                left_height = heights.get(node.left, 0)
                right_height = heights.get(node.right, 0)
                
                # Diameter through this node = left height + right height
                max_diameter = max(max_diameter, left_height + right_height)
                
                # Store height of current node for its parent
                heights[node] = 1 + max(left_height, right_height)
            else:
                # Pre-order: re-push with flag set to True, then push children
                stack.append((node, True))
                if node.right:
                    stack.append((node.right, False))
                if node.left:
                    stack.append((node.left, False))
        
        return max_diameter