import functools


class Solution:
    @functools.cache
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 1
        if n < 0:
            return 0
        return self.climbStairs(n - 2) + self.climbStairs(n - 1)
