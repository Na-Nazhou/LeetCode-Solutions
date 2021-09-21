"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        if head is None:
            head = Node(insertVal)
            head.next = head
            return head
        
        curr = head
        while curr.next:
            if curr.next.val < curr.val: # tail
                if insertVal >= curr.val or insertVal <= curr.next.val:
                    node = Node(insertVal)
                    node.next = curr.next
                    curr.next = node
                    break
                    
            if curr.val < insertVal and curr.next.val >= insertVal or (curr.next == head):
                node = Node(insertVal)
                node.next = curr.next
                curr.next = node
                break
                
            curr = curr.next
        
        return head