# time-out O(n**3)
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()

        res = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            for j in range(i+1,len(nums)-1):
                if j > i+1 and nums[j-1] == nums[j]:
                    continue
                for k in range(j+1, len(nums)):
                    if k > j+1 and nums[k-1] == nums[k]:
                        continue
                    if nums[i]+nums[j]+nums[k] == 0:
                        res.append([nums[i], nums[j], nums[k]])
        return res
