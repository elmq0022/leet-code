class Solution:
    def climbStairs(self, n: int) -> int:
        res = [0] * (n + 2)
        res[0] = 1  # one way to get up zero stairs
        res[1] = 1  # one way to get up one stair
        res[2] = 2  # two ways to get up two stairs

        for i in range(3, n + 1):
            res[i] = res[i - 1] + res[i - 2]

        return res[n]
