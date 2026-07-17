class Node:
    def __init__(self, data, key):
        self.val = data
        self.key = key
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self._capacity = capacity
        self.cache = {}

        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(value, key)
        self.insert(self.cache[key])

        if len(self.cache) > self._capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]