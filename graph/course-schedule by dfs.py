from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)

        traced = set()
        visited = set()

        def dfs(start):
            if start in traced:
                return False
            if start in visited:
                return True

            traced.add(start)
            for end in graph[start]:
                if not dfs(end):
                    return False

            traced.remove(start)
            visited.add(start)
            return True

        for i in list(graph):
            if not dfs(i):
                return False

        return True
