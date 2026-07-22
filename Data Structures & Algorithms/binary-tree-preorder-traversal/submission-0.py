# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []

        self.preOrder(root, res)
        
        return res

    def preOrder(self, node, res):
        if not node:
            return

        res.append(node.val)
        self.preOrder(node.left, res)
        self.preOrder(node.right, res)