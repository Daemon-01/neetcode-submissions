class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        # Sentinel dummy nodes to make insertion/removal O(1)
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self._size = 0

    def append(self, node: Node):
        """Adds a node to the end (most recently used position) of this frequency list."""
        prev_node = self.tail.prev
        prev_node.next = node
        node.prev = prev_node
        node.next = self.tail
        self.tail.prev = node
        self._size += 1

    def pop(self, node: Node = None) -> Node:
        """Removes and returns a node. If no node is specified, removes the least recently used (head.next)."""
        if self._size == 0:
            return None
        
        if node is None:
            node = self.head.next
            
        node.prev.next = node.next
        node.next.prev = node.prev
        self._size -= 1
        return node

    def __len__(self):
        return self._size


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}        # Maps key -> Node
        self.freq_map = {}     # Maps frequency -> DoublyLinkedList
        self.min_freq = 0      # Track the minimum frequency for O(1) eviction

    def _update_frequency(self, node: Node):
        """Helper to increment a node's frequency and move it to the correct frequency list."""
        freq = node.freq
        
        # Remove from current frequency list
        self.freq_map[freq].pop(node)
        
        # If the current minimum frequency list is empty, increment min_freq
        if freq == self.min_freq and len(self.freq_map[freq]) == 0:
            self.min_freq += 1
            
        # Update node frequency
        node.freq += 1
        new_freq = node.freq
        
        # Add to the new frequency list
        if new_freq not in self.freq_map:
            self.freq_map[new_freq] = DoublyLinkedList()
        self.freq_map[new_freq].append(node)

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self._update_frequency(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._update_frequency(node)
        else:
            # Evict LFU node if capacity is reached
            if len(self.cache) >= self.capacity:
                lfu_list = self.freq_map[self.min_freq]
                evicted_node = lfu_list.pop()  # Removes the LRU node from LFU list
                del self.cache[evicted_node.key]
                
            # Insert the new node
            new_node = Node(key, value)
            self.cache[key] = new_node
            
            # New nodes always start with frequency 1
            self.min_freq = 1
            if 1 not in self.freq_map:
                self.freq_map[1] = DoublyLinkedList()
            self.freq_map[1].append(new_node)