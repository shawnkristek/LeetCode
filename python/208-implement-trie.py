from collections import defaultdict, deque

class Solution:
    def __init__(self):
        self.children = defaultdict()
        self.eow = False

    def insert(self, word: str) -> None:
        letters = deque(word)
        node = self

        while letters:
            # grab next letter in word
            c = letters.popleft()
            # if letter in pointers, next node
            if c in node.children:
                node = node.children[c]
            # create new node and add to children of current node
            else:
                node.children[c] = Trie()
                # next node
                node = node.children[c]

        # last node is end-of-word
        node.eow = True

    def search(self, word: str) -> bool:
        letters = deque(word)
        node = self

        while letters:
            c = letters.popleft()
            if c in node.children:
                node = node.children[c]
            else:
                return False

        return node.eow

    def startsWith(self, prefix: str) -> bool:
        letters = deque(prefix)
        node = self

        while letters:
            c = letters.popleft()
            if c in node.children:
                node = node.children[c]
            else:
                return False

        return True

class NeetNode:
    def __init__(self):
        self.children = [None] * 26
        self.end = False

class NeetSolution:
    def __init__(self):
        self.root = NeetNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            i = ord(c) - ord('a')
            if curr.children[i] == None:
                curr.children[i] = NeetNode()
            curr = curr.children[i]
        curr.end = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            i = ord(c) - ord('a')
            if curr.children[i] == None:
                return False
            curr = curr.children[i]
        return curr.end

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            i = ord(c) - ord('a')
            if curr.children[i] == None:
                return False
            curr = curr.children[i]
        return True

# test

trie = NeetSolution()
trie.insert("apple")
print( trie.search("apple") == True )
print( trie.search("app") == False )
print( trie.startsWith("app") == True )
trie.insert("app")
print( trie.search("app") == True )