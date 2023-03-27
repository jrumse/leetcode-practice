class Solution:
    def climbStairs(self, n: int) -> int:
        # set both to 1
        # one way to get to 1
        one = 1
        two = 1
        # This solution is harder to visualize but it basically generates the fibonacci sequence
        for i in range(0, n - 1):
            # set temp = one's old value
            temp = one
            # one now equals the steps it takes to get to one + the steps it takes to get to two
            one = one + two
            # two is now one's old value
            two = temp
        # one will always be the highest to return one
        return one