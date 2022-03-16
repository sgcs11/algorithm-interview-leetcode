# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    answer=True
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return -1
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            if left - right > 1 or left - right < -1:
                self.answer=False
            
            return max(left, right) + 1

        dfs(root)
        return self.answer