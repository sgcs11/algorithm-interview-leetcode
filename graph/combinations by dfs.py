class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        results = []
        def dfs(elements, start):
            if len(elements) == k:
                results.append(elements[:])
                return

            for i in range(start + 1, n + 1):
                elements.append(i)
                dfs(elements, i)
                elements.pop()

        dfs([], 0)
        return results