class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Call the recursive balance check function
        checkmate = self.balanceCheck(root)
        # Returned is balanced boolean
        return checkmate[0]
    
    # bool: is balanced, int: height of sub tree
    def balanceCheck(self, root: Optional[TreeNode]) -> [bool, int]:
        # Base Case: Root is Null
        if root == None:
            return [True, 0]

        # Get the height and validity of the left side
        left = self.balanceCheck(root.left)
        # Get the height and validity of the right side
        right = self.balanceCheck(root.right)

        # Return the info
        return [
            # difference between left and right can be at most 1
            # left subtree needs to be valid
            # right subtree needs to be valid
            abs(left[1] - right[1]) <= 1 and left[0] and right[0],
            # calculate height of subtree (max of the left and right side)
            # must add 1 to accomidate for current node
            max(left[1], right[1]) + 1
        ]