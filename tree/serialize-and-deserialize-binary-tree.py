# Definition for a binary tree node.
from collections import deque
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        q = deque([root])
        res = ['#']
        
        while q:
            node = q.popleft()
                
            if node:
                q.append(node.left)
                q.append(node.right)
                
                res.append(node.val)
            else:
                res.append('#')
        return ' '.join(map(str,res))
            

    def deserialize(self, data):
        if data == '# #':
            return None
        
        nodes = data.split()
        
        root = TreeNode(int(nodes[1]))
        q = deque([root])
        idx = 2
        while q:
            node = q.popleft()
            if nodes[idx] is not '#':
                node.left = TreeNode(int(nodes[idx]))
                q.append(node.left)
            idx+=1
            
            if nodes[idx] is not '#':
                node.right = TreeNode(int(nodes[idx]))
                q.append(node.right)
            idx+=1
        
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))