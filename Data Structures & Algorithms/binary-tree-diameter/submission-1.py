# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        def maxDepth(root):
            if not root:
                return 0
            left = 1 + maxDepth(root.left)
            right = 1 + maxDepth(root.right)
            self.diameter = max(self.diameter, (right + left) - 2)
            return max(left,right)

        maxDepth(root)
        return self.diameter




