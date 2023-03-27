class Solution:
    def climbStairs(self, n: int) -> int:
        even = 2
        odd = 1

        if n == 1:
            return 1

        if n == 2:
            return 2

        for i in range(2, n):
            if (i + 1) % 2 == 0:
                even = even + odd
            if (i + 1) % 2 == 1:
                odd = even + odd
           

        return max(even, odd)