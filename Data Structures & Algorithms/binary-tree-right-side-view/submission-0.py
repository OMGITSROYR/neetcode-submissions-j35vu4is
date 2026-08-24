# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # right side means it's own level and no right child
        # at every node check if it is the rightest child on the level
        self.res = []
        self.levelTaken = set()
        self.dfs(root,0)

        return self.res

    def dfs(self,root,level):
        if not root:
            return
        
        if level not in self.levelTaken:
            self.res.append(root.val)
            self.levelTaken.add(level)

        self.dfs(root.right,level+1)
        level -= 0
        self.dfs(root.left,level+1)




