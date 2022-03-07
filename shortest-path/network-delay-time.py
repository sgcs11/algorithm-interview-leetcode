from collections import defaultdict
from heapq import heappush, heappop


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for x, y, cost in times:
            graph[x].append((y, cost))

        dist = defaultdict(int)
        q = [(0, k)]

        while q:
            srcDist, src = heappop(q)
            if src not in dist:
                dist[src] = srcDist
                for dest, cost in graph[src]:
                    heappush(q, (srcDist + cost, dest))

        if len(dist) == n:
            return max(dist.values())
        return -1