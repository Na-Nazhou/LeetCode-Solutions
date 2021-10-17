# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        a = headA
        b = headB
        
        swap_a = False
        
        while a != b:
            if not a.next:
                if swap_a:
                    return None
                
                swap_a = True
            
            a = a.next or headB
            b = b.next or headA
        
        return a