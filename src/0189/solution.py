from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        k = k % len(nums)
        len_left = len(nums) - k

        right = nums[len_left : len_left + k]
        nums[k:] = nums[:len_left]
        nums[0:k] = right
