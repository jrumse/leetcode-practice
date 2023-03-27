class Solution:
    memo = {}
    def climbStairs(self, n: int) -> int:
        # If you hit 0 you found a way
        # If you go under 0 you did not find a way
        if n == 0:
            return 1
        elif n < 0:
            return 0
        
        # Find out if oneSteppa and twoSteppa are a solution
        if not (n-1) in self.memo:
            self.memo[n - 1] = self.climbStairs(n - 1)
        if not (n - 2) in self.memo:
            self.memo[n - 2] = self.climbStairs(n - 2)

        # return the ways
        return self.memo[n - 1] + self.memo[n - 2]