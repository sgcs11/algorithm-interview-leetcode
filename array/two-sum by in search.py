class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i, n in enumerate(nums):
            complement = target - n

            if complement in nums[i + 1:]:
                return [i, nums[i + 1:].index(complement) + (i + 1)]
