#책의 풀이는 잘못 되어 있다. 시간초과 문제 발생
import heapq
from collections import defaultdict


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)

        for a, b, c in flights:
            graph[a].append((b, c))

        dist = [[float('inf')] * (k + 1) for i in range(n)]
        dist[src][0] = 0

        q = []
        for dest, cost in graph[src]:
            dist[dest][0] = cost
            heapq.heappush(q, (cost, dest, 0))

        while q:
            srcDist, src, level = heapq.heappop(q)
            if level == k or dist[src][level] < srcDist:
                continue
            for dest, cost in graph[src]:
                if dist[dest][level + 1] > srcDist + cost:
                    dist[dest][level + 1] = srcDist + cost
                    heapq.heappush(q, (dist[dest][level + 1], dest, level + 1))

        return min(dist[dst]) if min(dist[dst]) != float('inf') else -1