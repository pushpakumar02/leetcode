class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left = self.right = Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next , nxt.prev = nxt, prev

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev =  node
        node.next , node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)



### Intuition and Approach for `LRUCache`

#### Intuition

# The Least Recently Used (LRU) cache needs to efficiently support the following operations:
# 1. **Get a value by key**: This operation should return the value associated with the key if it exists in the cache and also update the key's position to indicate it was recently accessed.
# 2. **Put a key-value pair into the cache**: This operation should add the key-value pair to the cache. If the cache exceeds its capacity, the least recently used item should be removed.

# To achieve these requirements, we use a combination of a hashmap (for O(1) access) and a doubly linked list (to maintain the order of usage).

# #### Approach

# 1. **Data Structures**:
#    - **HashMap (`cache`)**: Stores key-node pairs for O(1) access to any node.
#    - **Doubly Linked List**: Helps maintain the order of usage. The most recently used item will be near the head (right), and the least recently used item will be near the tail (left).

# 2. **Initialization**:
#    - Create a dummy head (`left`) and a dummy tail (`right`) of the doubly linked list. These make it easier to handle edge cases when adding or removing nodes.
#    - Initialize the cache with a given capacity.

# 3. **Helper Functions**:
#    - **Remove Node (`remove`)**: Detaches a node from the linked list.
#    - **Insert Node (`insert`)**: Inserts a node at the most recently used position (before the tail).

# 4. **Get Operation**:
#    - If the key exists in the cache, remove the node from its current position and insert it back at the most recently used position. Return the value of the node.
#    - If the key does not exist, return -1.

# 5. **Put Operation**:
#    - If the key already exists in the cache, remove its current node.
#    - Add the new key-value pair to the cache and insert it at the most recently used position.
#    - If the cache exceeds its capacity, remove the least recently used node (just after the head) and delete its entry from the hashmap.

# #### Time Complexity
# - **Overall**: \(O(1)\) for both `get` and `put` operations, due to the efficient data structures used (hashmap and doubly linked list).

# #### Space Complexity
# - **Overall**: \(O(capacity)\) where capacity is the maximum number of key-value pairs the cache can hold.

# ### Summary

# - **HashMap**: Ensures O(1) time complexity for accessing elements.
# - **Doubly Linked List**: Maintains the order of usage, allowing O(1) insertion and removal of nodes.
# - **Efficient Design**: The combination of these data structures allows the LRU cache to meet the requirements efficiently.

# This approach ensures that both `get` and `put` operations are performed in constant time, making it highly efficient for use cases requiring frequent access and updates to the cache.