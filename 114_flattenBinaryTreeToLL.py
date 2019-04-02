class Solution:
    """Iterative solution below"""
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        stack = []
        current = root
        
        while current:
            if current.right:
                stack.append(current.right)
            
            if current.left:
                current.right = current.left
                current.left = None
            
            elif stack:
                current.right = stack.pop()
            
            else:
                return
            
            current = current.right