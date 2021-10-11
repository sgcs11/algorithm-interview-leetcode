class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(index):
            if index == len(nums):
                return [[]]

            res = dfs(index + 1)
            for arr in res[:]:
                res.append([nums[index]] + arr)

            return res

        return dfs(0)