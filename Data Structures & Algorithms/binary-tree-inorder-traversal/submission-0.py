# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.traversal(root, result)

        return result


    def traversal(self, node, result):
        if not node:
            return
        self.traversal(node.left, result)
        result.append(node.val)
        self.traversal(node.right, result)