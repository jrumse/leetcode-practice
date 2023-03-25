class Solution:
    def firstBadVersion(self, n: int) -> int:
        return self.detectBadVersion(1, n)
    
    def detectBadVersion(self, left: int, right: int):
        if isBadVersion(right) and not isBadVersion(right - 1):
            return right

        midpoint = left + ((right - left) // 2)

        # base case
        if isBadVersion(midpoint):
            if not isBadVersion(midpoint - 1):
                return midpoint
            else:
                return self.detectBadVersion(left, midpoint)
        else:
            return self.detectBadVersion(midpoint, right)