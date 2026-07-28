# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.goodNodes = 0
        self.maxNodes(root, root.val)
        return self.goodNodes

    def maxNodes(self, node, maxVal):
        if not node:
            return 0
        
        if maxVal <= node.val:
            self.goodNodes += 1
            maxVal = node.val
        self.maxNodes(node.left, maxVal)
        self.maxNodes(node.right, maxVal)