class LRUCache:

    def __init__(self, capacity: int):
        self.head = None # value: value
        self.tail = None
        self.map = {} # key: key; value: node
        self.cap = capacity

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        
        val = self.map[key].val[1]
        self.put(key, val)
        
        return val
    
    def delete(self, key: int):
        if key not in self.map:
            return
        
        node = self.map[key]
            
        if node.prev is None: # node is head
            self.head = self.head.next
        
        if node.next is None: # node is tail
            self.tail = self.tail.prev
        
        if node.prev is not None:
            node.prev.next = node.next
        
        if node.next is not None:
            node.next.prev = node.prev
        
        node.next = None
        node.prev = None
        
        self.map.pop(key)
        
    def deleteHead(self):
        if self.head is None:
            return
        if self.tail is self.head:
            self.tail = None
            
        self.map.pop(self.head.val[0])
        
        self.head.next = None
        self.head = self.head.next
        
    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.delete(key)
        
        if len(self.map) == self.cap:
            self.delete(self.head.val[0])
        
        node = ListNode((key, value))
        if self.head is None:
            self.head = node
        if self.tail is not None:
            node.prev = self.tail
            self.tail.next = node
        
        self.tail = node
        
        self.map[key] = node
        

class ListNode:
    
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)