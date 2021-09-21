class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)-2):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                temp_sum = nums[i] + nums[left] + nums[right]
                if temp_sum < 0:
                    left += 1
                elif temp_sum > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1

        return res
