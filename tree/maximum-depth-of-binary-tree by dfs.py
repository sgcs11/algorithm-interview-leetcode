# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def get_depth(self, node:TreeNode, depth:int) -> int:
        if not node:
            return depth
        
        left_value = self.get_depth(node.left, depth+1)
        right_value = self.get_depth(node.right, depth+1)
        return max(left_value, right_value)
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.get_depth(root,0)