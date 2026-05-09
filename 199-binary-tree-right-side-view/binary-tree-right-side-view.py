class Solution:
    
    def rightSideView(self, root):
        
        ans = []
        
        def dfs(node, level):
            
            if not node:
                return
            
            # First node at this level
            if level == len(ans):
                ans.append(node.val)
            
            # Go right first
            dfs(node.right, level + 1)
            dfs(node.left, level + 1)
        
        dfs(root, 0)
        
        return ans