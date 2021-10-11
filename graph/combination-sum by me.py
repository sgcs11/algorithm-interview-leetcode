class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        prev_elements = []

        def dfs(start):
            if sum(prev_elements) > target:
                return
            elif sum(prev_elements) == target:
                results.append(prev_elements[:])
                return

            for i in range(start, len(candidates)):
                prev_elements.append(candidates[i])
                dfs(i)
                prev_elements.pop()

        dfs(0)
        return results