# Structure of binary tree node
'''
class Node:
    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None
'''

class Solution:
    def verticalSum(self, root):
        # code here
        mp = {}
        def dfs(node, hd):
            if not node:
                return
            mp[hd] = mp.get(hd, 0) + node.data
            dfs(node.left, hd - 1)
            dfs(node.right, hd + 1)
            
        dfs(root, 0) 
        ans = []
        
        for hd in sorted(mp):
            ans.append(mp[hd])
            
        return ans    
        
            
            
            
            
            
            
            
            
            
            
            
            
            
