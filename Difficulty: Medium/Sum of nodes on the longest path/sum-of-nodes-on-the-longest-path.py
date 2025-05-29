'''
class Node:
    def __init__(self, val):
        self.data=val
        self.left=None
        self.right=None
'''
class Solution:
    def sumOfLongRootToLeafPath(self, root):
        
        def dfs(node):
            if node is None:
                return 0, 0
            depth, sumi = max(dfs(node.left), dfs(node.right))
            return (depth + 1, sumi + node.data)
        
        return dfs(root)[1]