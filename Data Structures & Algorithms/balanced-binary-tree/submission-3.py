# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #abs(height left - height right > 1)
        if not root:
            return True 
        
        h_left = self.height(root.left)
        h_right = self.height(root.right)
        print(f"left={h_left}")
        print(f"right={h_right}")

        if abs(h_left-h_right) > 1:
            return False
        
        if not self.isBalanced(root.left) or not self.isBalanced(root.right):
            return False

        return True 


    def height(self,root):
        if not root:
            return 0

        left = self.height(root.left)
        right = self.height(root.right)
            
        return 1 + max(left,right)