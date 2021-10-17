"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        
        # empty
        # x -> insertVal -> y (x <= y)
        # x -> insertVal (tail)
        # insertVal -> x (head)
        
        node = Node(insertVal)
        
        if head is None:
            node.next = node
            return node
        
        curr = None
        while curr != head:
            if curr is None:
                curr = head
            
            if insertVal >= curr.val and insertVal <= curr.next.val:
                break
                
            if curr.val > curr.next.val and (insertVal >= curr.val or insertVal <= curr.next.val):
                break
            
            curr = curr.next
        
        # Insert after curr
        node.next = curr.next
        curr.next = node
        
        return head
            