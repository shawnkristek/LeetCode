from collections import deque, defaultdict

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def values(self):
        values = [self.val]
        next = self.next
        while next:
            values.append(next.val)
            next = next.next

        return values

    def __repr__(self):
        return str(self.values())

    def build(self, values: list[int]) -> 'ListNode':
        '''
        Given an array of ints,
        Return a linked-list 
        [n1, n2, n3] -> n1->n2->n3
        '''
        next = None
        for v in reversed(values):
            next = ListNode(v, next)

        return next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def values(self):
        values = []
        q = deque([self])
        
        while q:
            # pop next node for processing
            curr = q.popleft()

            if curr:
                # append node value
                values.append(curr.val)
    
                # add children to stack for processing
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    # if right child only
                    if not curr.left:
                        q.append(None)
                    q.append(curr.right)
            else:
                values.append(None)


        return values

    def __repr__(self):
        return str(self.values())


    def build(self, values: list[int]) -> 'TreeNode':
        if not values:
            return None

        head = TreeNode(values.pop(0), None, None)
        q = deque([head])

        while q:
            # pop next node for updates
            curr = q.popleft()

            # update left,right pointers of current node
            if values:
                if values[0] is None:
                    values.pop(0)
                else:
                    curr.left = TreeNode(values.pop(0), None, None)
            if values:
                if values[0] is None:
                    values.pop(0)
                else:
                    curr.right = TreeNode(values.pop(0), None, None)

            # append new nodes to q
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)

        return head

class TrieNode:
    def __init__(self):
        self.children = defaultdict()
        self.eow = False

    def __traverse(self, s: str) : # -> tuple(bool, 'Trie')
        letters = deque(s)
        node = self

        while letters:
            c = letters.popleft()
            if c in node.children:
                node = node.children[c]
            else:
                return (False, node)

        return (True, node)

    def insert(self, word: str) -> None:
        letters = deque(word)
        node = self

        while letters:
            c = letters.popleft()
            if c in node.children:
                node = node.children[c]
            else:
                node.children[c] = TrieNode()
                node = node.children[c]

        # last node is end-of-word
        node.eow = True

    def search(self, word: str) -> bool:
        found, node = self.__traverse(word)

        return node.eow and found 

    def startsWith(self, prefix: str) -> bool:
        found, node = self.__traverse(prefix)

        return found