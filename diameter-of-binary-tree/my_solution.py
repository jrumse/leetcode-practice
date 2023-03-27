class Solution:
    # Call find function and return it's maximum diameter
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diam = self.findDiameter(root)
        return diam[1]
        
    # First index of return value is the height of the tree
    # Second index of return value is the maximum diameter found
    def findDiameter(self, root: Optional[TreeNode]) -> [int, int]:
        # at a null leaf, there is no height or diameter to find
        # this is a base case
        if root == None:
            return [0, 0]
        
        # get the height and max diameter of the left and right side
        left = self.findDiameter(root.left)
        right = self.findDiameter(root.right)

        # Return the height and diameter
        return [
            # this will return the larger depth of the left and right side, and add 1 to account for current node
            # calculates the height
            1 + max(left[0], right[0]),
            # calculate the diameter with the left and right heights
            # then, take the maximum diameter of the left and right sides
            # determine if the current diameter is greater than the maximum diameter of the left and right sides
            max(left[0] + right[0], max(left[1], right[1]))
        ]