# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.cnt = 0
        self.res = 0
        self.dfs(root, k)
        return self.res
        
    def dfs(self, node: TreeNode, k: int):

        if not node:
            return

        self.dfs(node.left, k)
        self.cnt += 1
        if self.cnt == k:
            self.res = node.val
            return
        self.dfs(node.right, k)
