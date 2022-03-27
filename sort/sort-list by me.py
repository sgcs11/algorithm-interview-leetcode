# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr
            
            res = []
            mid = len(arr)//2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])
            
            i, j = 0, 0
            while i < len(left) or j < len(right):
                left_value = left[i] if i < len(left) else float('inf')
                right_value = right[j] if j < len(right) else float('inf')
                
                if left_value <= right_value:
                    i += 1
                    res.append(left_value)
                else:
                    j += 1
                    res.append(right_value)
                    
            return res
        arr = []
        node = head
        
        while node:
            arr.append(node.val)
            node = node.next
        
        
        arr = merge_sort(arr)
        i = 0
        node = head
        while node:
            node.val = arr[i]
            i += 1
            node = node.next
        
        return head