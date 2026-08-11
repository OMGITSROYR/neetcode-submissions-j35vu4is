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

        queue = deque()
        queue.append((root,1))
        visited = []

        while queue:
            node,level = queue.popleft()
            visited.append((node.val,level))

            if node.left:
                queue.append((node.left,level+1))
            if node.right: 
                queue.append((node.right,level+1))
        
        res = [[] for _ in range(visited[-1][1])]

        for val, level in visited:
            res[level - 1].append(val)

        return res
