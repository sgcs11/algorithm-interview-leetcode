# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        temp = res

        while l1 or l2:
            l1_value = l1.val if l1 else float('inf')
            l2_value = l2.val if l2 else float('inf')
            if l1_value <= l2_value:
                temp.next = ListNode(l1.val, None)
                l1 = l1.next
            else:
                temp.next = ListNode(l2.val, None)
                l2 = l2.next
            temp = temp.next

        return res.next
