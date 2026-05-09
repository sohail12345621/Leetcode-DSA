class Solution:
    
    def __init__(self):
        self.prev = None
    
    def flatten(self, root):
        
        if not root:
            return
        
        # First flatten right
        self.flatten(root.right)
        
        # Then flatten left
        self.flatten(root.left)
        
        # Connect current node to previous node
        root.right = self.prev
        root.left = None
        
        # Move prev to current node
        self.prev = root