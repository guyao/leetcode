"""
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
"""

#Double Linked List
#TODO
class Node(object):
    def __init__(self, key, val):
        self.prev = None
        self.next = None
        self.key = key
        self.val = val

    def __repl__(self):
        return str(self.key), ": ",str(self.val)

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.key_node = {}
        self.cache_head = Node(None, None)
        self.count = 0

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.key_node:
            node = self.key_node[key]
            self.delete_node(node)
            self.add_to_head(node)
            return node.val
        else:
            return -1
        
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.key_node:
            node = self.key_node[key]
            node.val = value
            self.update_node(node)
        else:
            self.count += 1
            if self.count > self.capacity:
                node_to_del = self.cache_head.prev
                self.delete_node(node_to_del)
                self.count -= 1
            node = Node(key, value)
            self.add_to_head(node)
            self.key_node[key] = node

    def update_node(self, node):
        self.delete_node(node)
        self.add_to_head(node)

    def delete_node(self, node):
        if node.next is not None:
            prev = node.prev
            nxt = node.next
            prev.next = nxt
            nxt.prev = prev
        else:
            prev = node.prev
            prev.next = None
        self.key_node.pop(node.key)

    def add_to_head(self, node):
        if self.cache_head.next is not None:
            nxt = self.cache_head.next
            self.cache_head.next = node
            node.next = nxt
            nxt.prev = node
            node.prev = self.cache_head
        else:
            self.cache_head.next = node
            node.prev = self.cache_head
            self.cache_head.prev = node
            node.next = self.cache_head
        self.key_node[node.key] = node



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
