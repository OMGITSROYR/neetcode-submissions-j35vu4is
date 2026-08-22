# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # run a dfs for both, record the path, and then compare 
        path_p = self.dfs(root, p.val)
        path_q = self.dfs(root, q.val)

        lca = None
        for a,b in zip(path_p,path_q):
            if a == b:
                lca = a
            else:
                break
        
        return lca

    def dfs(self,root,target,path=None):
        if path is None:
            path = []

        if not root:
            return None

        path.append(root)

        if root.val == target:
            return list(path)

        result = self.dfs(root.left, target, path)
        if result:
            return result

        result = self.dfs(root.right, target, path)
        if result:
            return result

        path.pop()
        return None