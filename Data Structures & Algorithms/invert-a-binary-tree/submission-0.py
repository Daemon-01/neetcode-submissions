# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        self.invert(root)
        return root

    def invert(self, node):
        if not node:
            return None
        T1 = node.left
        node.left = node.right
        node.right = T1

        self.invert(node.left)
        self.invert(node.right)
