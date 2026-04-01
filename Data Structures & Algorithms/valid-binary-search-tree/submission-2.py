# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

       return self.dfs(root, float('inf'), float('-inf'))

    def dfs(self, node: TreeNode, upper: int, lower: int):

        if(node == None):
            return True

        #violations
        if node.val >= upper:
            return False
        
        if node.val <= lower:
            return False

        return self.dfs(node.left, node.val, lower) and self.dfs(node.right, upper, node.val)



            

            
            


        