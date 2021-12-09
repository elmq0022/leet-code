from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        results = []

        def perm(nums, result=None):
            if not nums and result:
                results.append(result)

            if not result:
                result = []

            for i, item in enumerate(nums):
                perm(nums[:i] + nums[i + 1 :], [r for r in result] + [item])

        perm(nums)

        return results
