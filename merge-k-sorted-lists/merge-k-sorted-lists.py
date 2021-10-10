# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h = []
        i = 0
        for head in lists:
            if head is None:
                continue
            heapq.heappush(h, (head.val, i, head))
            i += 1
        
        dummy_head = ListNode()
        prev = dummy_head
        while h:
            _, _, node = heapq.heappop(h)
            prev.next = node
            prev = node
            
            if node.next is not None:
                heapq.heappush(h, (node.next.val, i, node.next))
                i += 1
        
        return dummy_head.next
            