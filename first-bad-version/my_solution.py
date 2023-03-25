# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # if n and not n - 1
        if isBadVersion(n) and not isBadVersion(n - 1):
            return n

        # Set Left Pointer
        left = 1
        # Set Right Pointer
        right = n

        while left < right:
            # calculate midpoint
            midpoint = left + ((right - left) // 2)
            # if the midpoint is bad
            if isBadVersion(midpoint):
                # if midpoint is the first bad version
                if midpoint - 1 >= 0 and not isBadVersion(midpoint - 1):
                    return midpoint
                else:
                    right = midpoint
            # midpoint is not bad
            else:
                left = midpoint