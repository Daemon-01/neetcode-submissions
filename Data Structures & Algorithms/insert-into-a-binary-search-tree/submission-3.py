# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root: 
            node = TreeNode(val)
            return node
        self.insert(root, val)
        return root

    def insert(self, curr, val):
        if curr.val > val:
            if not curr.left:
                node = TreeNode(val)
                curr.left = node
            else:
                return self.insert(curr.left, val)
        elif curr.val < val:
            if not curr.right:
                node = TreeNode(val)
                curr.right = node
            else:
                return self.insert(curr.right, val)