# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        left_height = self.treeLength(root.left)
        right_height = self.treeLength(root.right)
        if abs(left_height - right_height) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def treeLength(self,root):
        if not root:
            return 0
        stack = [(root,1)]
        maxDepth = 0

        while stack:
            node,depth = stack.pop()
            maxDepth = max(maxDepth,depth)
            if node.left:
                stack.append((node.left,depth+1))
            if node.right:
                stack.append((node.right,depth+1))
        
        return maxDepth
        