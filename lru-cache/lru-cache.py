class ListNode:
    
    def __init__(self, key, val):
        self.prev = None
        self.next = None
        self.key = key
        self.val = val

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {} # key: key; value: ListNode
        self.head = None
        self.tail = None

    def get(self, key: int) -> int:
        if key in self.map:
            self.put(key, self.map[key].val)
            return self.map[key].val
        else:
            return -1
        
    def delete(self, key: int):
        if key not in self.map:
            return
        
        node = self.map[key]
        if self.head == node:
            self.head = self.head.next
        if self.tail == node:
            self.tail = self.tail.prev
        
        prev = node.prev
        next = node.next
        
        if prev is not None:
            prev.next = next
        if next is not None:
            next.prev = prev
        
        del self.map[key]

    def put(self, key: int, value: int) -> None:
        self.delete(key)
        
        if len(self.map) >= self.capacity:
            self.delete(self.head.key)
        
        node = ListNode(key, value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        
        self.map[key] = node
        
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)