from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = []
        left, right = 0, len(nums) - 1

        while left <= right:
            square_left = nums[left] ** 2
            square_right = nums[right] ** 2
            if square_left > square_right:
                result.append(square_left)
                left += 1

            else:
                result.append(square_right)
                right -= 1

        return result[::-1]
