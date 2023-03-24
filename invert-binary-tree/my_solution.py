class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # Base Case
        if root == None:
            return None

        # Intermediate node
        # Necessary so that we don't accidentally set "right" and then pass "right" 
        # which circumvents overriding everying with "right"
        intermediate = TreeNode()
        intermediate.val = root.val
        
        # Swap current node's right and left with dfs
        intermediate.right = self.invertTree(root.left)
        intermediate.left = self.invertTree(root.right)

        return intermediate