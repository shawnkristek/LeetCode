from collections import defaultdict, deque

#class WordDictionary:
class Solution:
    def __init__(self):
        self.children = defaultdict()
        self.eow = False

    def addWord(self, word: str) -> None:
        letters = deque(word)
        node = self

        while letters:
            c = letters.popleft()
            if c in node.children:
                node = node.children[c]
            else:
                child = Solution()
                node.children[c] = child
                node = child

        node.eow = True

        return None

    def search(self, word: str) -> bool:
        letters = deque(word)
        node = self

        while letters:
            c = letters.popleft()
            if c in node.children:
                node = node.children[c]
            elif c == '.':
                for child in node.children.values():
                    if child.search("".join(letters)):
                        return True
                else:
                    return False
            else:
                return False

        return node.eow 

class NeetNode:
    def __init__(self):
        self.children = {}
        self.word = False

class NeetSolution:
    def __init__(self):
        self.root = NeetNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = NeetNode()
            cur = cur.children[c]
        cur.word = True
    
    def search(self, word: str) -> bool:
        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.word

        return dfs(0, self.root)

class WordDictionary:   
    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        curr = self.trie
        for char in word:
            if char not in curr:
                curr[char] = {}
            curr = curr[char]
        curr['#'] = True        

    def search(self, word: str) -> bool:
        return self.match(self.trie, word, 0)
    
    def match(self, node, word, index):
        if index == len(word): 
            return '#' in node
        
        if word[index]=='.':
            for child in node:
                if child!='#' and self.match(node[child], word, index+1):
                    return True 
            return False 
            
        if word[index] not in node: 
            return False        
        return self.match(node[word[index]], word, index+1)    


# test

sol = NeetSolution()
sol.addWord("bad")
sol.addWord("dad")
sol.addWord("mad")

print( sol.search("pad") == False )
print( sol.search("bad") == True )
print( sol.search(".ad") == True )
print( sol.search("b..") == True )

sol2 = NeetSolution()
sol2.addWord("at")
sol2.addWord("and")
sol2.addWord("an")
sol2.addWord("add")

print( sol2.search("a") == False )
print( sol2.search(".at") == False )

sol2.addWord("bat")

print( sol2.search(".at") == True )
print( sol2.search("an.") == True )
print( sol2.search("a.d.") == False )
print( sol2.search("b.") == False )
print( sol2.search("a.d") == True )
print( sol2.search(".") == False )