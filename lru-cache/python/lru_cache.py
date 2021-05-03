DUMMY = "DUMMY"


class ListNode:
    def __init__(self, key, value):
        self.value = value
        self.key = key
        self.next = None
        self.prev = None


dummy_node = ListNode(DUMMY, 0)


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.head = dummy_node
        self.tail = dummy_node
        self.table = {}

    def get(self, key):
        if key in self.table:
            self._update_to_recent(key)
            return self.table[key].value
        else:
            print("Key {} not found".format(key))

    def put(self, key, value):
        if key in self.table:
            self.table[key].value = value
            self._update_to_recent(key)
            return
        new_node = ListNode(key, value)

        self.table[key] = new_node

        if self.head.key == DUMMY:
            self.head = new_node
            self.tail = new_node
            return

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

        if len(self.table) > self.capacity:
            self._delete_tail()

    def _update_to_recent(self, key):
        node_to_update = self.table[key]
        # Do nothing if the node to update is head.
        if node_to_update == self.head:
            return

        assert len(self.table) > 1

        # 1. Connect the next and previous nodes of the node to update
        if node_to_update.prev:
            node_to_update.prev.next = node_to_update.next
        if node_to_update.next:
            node_to_update.next.prev = node_to_update.prev

        # 2. Update self.tail if node to update is the tail
        if node_to_update == self.tail:
            self.tail = node_to_update.prev

        # 3. Connect the node to update and the current self.head
        self.head.prev = node_to_update
        node_to_update.next = self.head

        # 4. Update self.head
        self.head = node_to_update

    def _delete_tail(self):
        node_to_be_deleted = self.tail
        if node_to_be_deleted.value == DUMMY:
            raise Exception("Cannot delete a dummy.")

        key = node_to_be_deleted.key
        del self.table[key]
        if len(self.table) == 1:
            self.head = dummy_node
            self.tail = dummy_node
            return

        assert len(self.table) > 1
        new_tail = self.tail.prev
        new_tail.next = None
        self.tail = new_tail


# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(2)
# print(obj.get(10))
obj.put(1, 10)
obj.put(2, 20)
# print(obj.get(1))
# print(obj.get(2))
obj.put(3, 30)
# obj.get(1)
obj.put(4, 40)
obj.put(5, 50)
print(obj.get(1))
print(obj.get(2))
print(obj.get(3))
print(obj.get(4))
print(obj.get(5))
# obj = LRUCache(1)
# print(obj.put(1, 10))
# print(obj.get(1))
# print(obj.put(2, 20))
# print(obj.get(1))
# print(obj.get(2))
