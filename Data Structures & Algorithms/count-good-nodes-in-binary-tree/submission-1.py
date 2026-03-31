# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    res = 0
    def goodNodes(self, root: TreeNode) -> int:
        self.dfs(root, -101)
        return self.res

    def dfs(self, node: TreeNode, maxVal: int):
        
        if(node == None):
            return 

        if(node.val >= maxVal):
            maxVal = node.val
            self.res += 1

        self.dfs(node.left, maxVal)
        self.dfs(node.right, maxVal)




        
        