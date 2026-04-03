# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    pre_idx = 0
    indicies = {}

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
       for i in range(len(inorder)):
            self.indicies[inorder[i]] = i
       self.preorder = preorder
       self.inorder = inorder
       return self.dfs(0, len(inorder)-1)

    def dfs(self, l, r):

        if l>r:
            return None

        root_val = preorder[self.pre_idx]
        self.pre_idx += 1
        root = TreeNode(root_val)
        mid = self.indicies[root_val]
        root.left = self.dfs(l, mid -1)
        root.right = self.dfs(mid+1, r)
        return root




        