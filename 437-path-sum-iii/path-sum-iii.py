class Solution:
    
    def pathSum(self, root, targetSum):
        
        prefix = {0: 1}
        
        return self.dfs(root, 0, targetSum, prefix)
    
    
    def dfs(self, node, currSum, target, prefix):
        
        if not node:
            return 0
        
        currSum += node.val
        
        count = prefix.get(currSum - target, 0)
        
        prefix[currSum] = prefix.get(currSum, 0) + 1
        
        count += self.dfs(node.left, currSum, target, prefix)
        count += self.dfs(node.right, currSum, target, prefix)
        
        # Backtrack
        prefix[currSum] -= 1
        
        return count