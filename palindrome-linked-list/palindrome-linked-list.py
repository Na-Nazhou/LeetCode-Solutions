# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        slow_ptr = head # mid
        fast_ptr = head
        
        while fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        
        tail = self.reverse(slow_ptr)
        
        start = head
        end = tail
        
        while start and end:
            if start.val != end.val:
                return False
            start = start.next
            end = end.next
        
        slow_ptr.next = self.reverse(tail)
        
        return True
        
    # None <- 1 <- 2 <- 3 None
    def reverse(self, head):
        prev = None
        curr = head
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        
        return prev