from collections import defaultdict, deque

class Solution: # Trie class
    def __init__(self):
        self.children = defaultdict()
        self.eow = False

    def __traverse(self, s: str) : # -> tuple(bool, 'Solution')
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
                node.children[c] = Solution()
                node = node.children[c]

        # last node is end-of-word
        node.eow = True

    def search(self, word: str) -> bool:
        found, node = self.__traverse(word)

        return node.eow and found 

    def startsWith(self, prefix: str) -> bool:
        found, node = self.__traverse(prefix)

        return found

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

trie = Solution()
trie.insert("apple")
print( trie.search("apple") == True )
print( trie.search("app") == False )
print( trie.startsWith("app") == True )
trie.insert("app")
print( trie.search("app") == True )