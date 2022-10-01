class Node:
    def __init__(self, key: int, val: int):
        self.key, self.val = key, val
        self.prev = self.next = None

class NeetSolution:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left

    # remove node from list
    def remove(self, node: Node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = node.next, node.prev
        
    # insert node at right        
    def insert(self, node: Node):
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
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            # remove LRU node
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

# test

lru = NeetSolution(2)
print(lru.put(1,1) == None)
print(lru.put(2,2) == None)
print(lru.get(1) == 1)
print(lru.put(3,3) == None)
print(lru.get(2) == -1)
print(lru.put(4,4) == None)
print(lru.get(1) == -1)
print(lru.get(3) == 3)
print(lru.get(4) == 4)