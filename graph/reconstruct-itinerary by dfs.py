from collections import defaultdict

#위상 정렬의 개념으로 생각해보기
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for start, end in sorted(tickets, reverse=True):
            graph[start].append(end)

        route = []

        def dfs(start):
            while graph[start]:
                dfs(graph[start].pop())
            route.append(start)
            print(route)

        dfs("JFK")
        return route[::-1]