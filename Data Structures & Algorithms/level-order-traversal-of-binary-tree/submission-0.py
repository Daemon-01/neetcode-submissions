# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        nodesCollection = []
        q = deque([root])

        while q:
            size = len(q)
            levelNodes = []

            for _ in range(0,size):
                node = q.popleft()
                levelNodes.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            nodesCollection.append(levelNodes)
        return nodesCollection