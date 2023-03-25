class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Base case 1: both values are less than the root
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)

        # Base case 2: both values are more than the root
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)

        # Base case 3: root is in the middle of p and q
        # base case 4: root == p or root == q
        # both of these cases are covered by just returning root, bc the're both considered a found lca
        return root