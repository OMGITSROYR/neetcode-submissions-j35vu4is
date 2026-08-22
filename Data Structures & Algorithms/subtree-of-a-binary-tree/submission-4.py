# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # if the root and the children are the same
        # find the start of subroot by running a dfs
        if not root and not subRoot:
            return True
        elif root and not subRoot:
            return True
        elif not root and subRoot:
            return False
        
        if root.val == subRoot.val and self.isSame(root, subRoot):
            return True
        else:
            return self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)

        return False

    def isSame(self,root,subRoot):
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False

        if root.val != subRoot.val:
            return False

        left = self.isSame(root.left,subRoot.left)
        right = self.isSame(root.right,subRoot.right)

        return left and right


