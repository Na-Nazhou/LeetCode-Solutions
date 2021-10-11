# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        fast_ptr = head
        for _ in range(n):
            fast_ptr = fast_ptr.next
        
        slow_ptr = head
        
        # Remove head
        if fast_ptr is None:
            return head.next
        
        while fast_ptr.next is not None:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next
        
        
        slow_ptr.next = slow_ptr.next.next
        
        return head