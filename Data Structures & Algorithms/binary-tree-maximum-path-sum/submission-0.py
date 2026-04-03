# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    res = -float('inf')
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.postOrder(root)
        return self.res
    
    def postOrder(self, root: TreeNode):
        if not root:
            return 0

        left = max(self.postOrder(root.left), 0)
        right = max(self.postOrder(root.right), 0)
        self.res = max(self.res, root.val+ left+right)

        return max(left,right) +root.val

        