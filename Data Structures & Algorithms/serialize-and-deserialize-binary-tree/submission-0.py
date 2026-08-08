# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:

    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        
        if not root:
            return "N"

        strRep = []
        q = deque([root])
        while q:
            
            node = q.popleft()
            if not node:
                strRep.append('N')
            else:
                strRep.append(str(node.val))

            if node:
                q.append(node.left)
                q.append(node.right)
            
        return ",".join(strRep)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        vals = data.split(",")
        if vals[0] == "N":
            return None

        root = TreeNode(int(vals[0]))
        q = deque([root])
        i = 0
        while q:

            node = q.popleft()

            i += 1
            if i < len(vals):
                if vals[i] == 'N':
                    node.left = None
                else:
                    node.left = TreeNode(int(vals[i]))
                    q.append(node.left)

            i+= 1
            if i < len(vals):
                if vals[i] == 'N':
                    node.right = None
                else:
                    node.right = TreeNode(int(vals[i]))
                    q.append(node.right)

        
        return root





