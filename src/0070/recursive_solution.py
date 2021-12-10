class Solution:
    cache = dict()

    def climbStairs(self, n: int) -> int:
        if n in self.cache:
            return self.cache[n]
        if n == 0:
            return 1
        if n < 0:
            return 0

        a = self.climbStairs(n - 2)
        b = self.climbStairs(n - 1)
        self.cache[n - 2] = a
        self.cache[n - 1] = b
        return a + b
