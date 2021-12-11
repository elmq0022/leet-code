from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        result = [0] * (n + 2)
        result[0] = 0
        result[1] = nums[0]

        for i in range(2, n + 1):
            result[i] = max(result[i - 2] + nums[i - 1], result[i - 1])

        return result[n]


class Solution2:
    def rob(self, nums: List[int]) -> int:
        h1, h2 = 0, 0

        for val in nums:
            # best decsion at "h3"
            h2, h1 = max(h1 + val, h2), h2

        return h2
