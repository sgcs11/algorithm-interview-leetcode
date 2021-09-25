# deque로 풀기
# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
#
# from collections import deque
#
#
# class Solution:
#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#         q = deque()
#
#         for lst in lists:
#             while lst:
#                 q.append(lst.val)
#                 lst = lst.next
#
#         q = deque(sorted(q))
#         head = temp = ListNode(None)
#         while q:
#             temp.next = ListNode(q.popleft())
#             temp = temp.next
#         return head.next


# priority queue로 풀기
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        q = []

        for lst in lists:
            while lst:
                q.append(lst.val)
                lst = lst.next

        heapq.heapify(q)
        head = temp = ListNode(None)
        while q:
            temp.next = ListNode(heapq.heappop(q))
            temp = temp.next
        return head.next

# 책 풀이 변형해서 품
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        root = result = ListNode(None)

        for i, lst in enumerate(lists):
            if lst:
                heapq.heappush(heap, (lst.val, i, lst))

        while heap:
            val, i, lst = heapq.heappop(heap)
            result.next = lst
            result = result.next
            if lst.next:
                heapq.heappush(heap, (lst.next.val, i, lst.next))

        return root.next
    