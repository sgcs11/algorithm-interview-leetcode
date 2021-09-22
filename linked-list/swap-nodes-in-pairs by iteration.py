# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = prev = ListNode()
        prev.next = head
        while head and head.next:
            a, b = head, head.next
            prev.next = b
            a.next = b.next
            b.next = a

            head = a.next
            prev = a

        return root.next
    