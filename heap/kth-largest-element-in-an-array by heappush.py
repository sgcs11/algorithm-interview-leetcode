import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = list()
        for num in nums:
            heapq.heappush(heap, -num)

        for _ in range(k - 1):
            heapq.heappop(heap)

        return -heapq.heappop(heap)