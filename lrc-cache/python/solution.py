class ListNode:
    def __init__(self, key, value):
        self.val = value
        self.key = key
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.size = 0
        self.table = {}
        self.head = None
        self.tail = None

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.table:
            value = self.table[key].val
            self._update(key, value)
            return value
        else:
            return -1

    def _insert_to_head(self, key, value):
        node = ListNode(key, value)
        if self.head:
            self.head.prev = node
            node.next = self.head
        self.head = node

        if not self.tail:
            self.tail = node
        self.table[key] = self.head

    def _remove_node(self, node):
        if self.tail == node and self.head == node:
            self.tail = None
            self.head = None
        elif self.tail == node:
            self.tail = node.prev
            if self.tail:
                self.tail.next = None
        elif self.head == node:
            self.head = node.next
            if self.head:
                self.head.prev = None
        else:
            if node.next:
                node.next.prev = node.prev
            if node.prev:
                node.prev.next = node.next

        del self.table[node.key]
        del node

    def _update(self, key, value):
        node = self.table[key]
        self._remove_node(node)
        self._insert_to_head(key, value)

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """

        if not self.head:
            self._insert_to_head(key, value)
            self.size = 1
        elif key in self.table:
            self._update(key, value)
        else:
            self._insert_to_head(key, value)
            self.size += 1

        if self.cap < self.size:
            self._remove_node(self.tail)
            self.size -= 1


# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(4)
print(obj.get(10))
print(obj.put(1, 10))
print(obj.put(2, 20))
print(obj.get(1))
print(obj.get(2))
print(obj.put(3, 30))
print(obj.put(4, 40))
print(obj.put(5, 50))
print("next output should be -1")
print(obj.get(1))
print(obj.get(2))
print(obj.get(3))
print(obj.get(4))
obj = LRUCache(1)
print(obj.put(1, 10))
print(obj.get(1))
print(obj.put(2, 20))
print(obj.get(1))
print(obj.get(2))
