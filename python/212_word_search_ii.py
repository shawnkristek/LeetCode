# from reuse import TrieNode, Trie

# class MySolution:
    # def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:

    #     root = Trie()

    #     for word in words:
    #         root.insert(word)

    #     ROWS, COLS = len(board), len(board[0])
    #     result, visit = set(), set()

    #     pass

class NeetNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        self.refs = 0

    def addWord(self, word):
        cur = self
        cur.refs += 1
        for c in word:
            if c not in cur.children:
                cur.children[c] = NeetNode()
            cur = cur.children[c]
            cur.refs += 1
        cur.isWord = True

    def removeWord(self, word):
        cur = self
        cur.refs -= 1
        for c in word:
            if c in cur.children:
                cur = cur.children[c]
                cur.refs -= 1

class NeetSolution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        root = NeetNode()
        for w in words:
            root.addWord(w)

        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()

        def dfs(r, c, node, word):
            if (
                r < 0
                or c < 0
                or r == ROWS
                or c == COLS
                or board[r][c] not in node.children
                or node.children[board[r][c]].refs < 1
                or (r, c) in visit
            ):
                return

            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                node.isWord = False
                res.add(word)
                root.removeWord(word)

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            visit.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        return list(res)

class Node:
    def __init__(self, end = 0):
        self.end = end
        self.kids = {}

class FoundSolution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        res, root, m, n = set(), Node(0), len(board), len(board[0])
        
        def setTrie(word):
            cur = root
            for w in word:
                if w not in cur.kids:
                    cur.kids[w] = Node()
                cur = cur.kids[w]
            cur.end = 1
            return
        
        def helper(i, j, root, visited, word):
            if root.end == 1: res.add(word)
            visited.add((i, j)) 

            for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                x, y = i + dx, j + dy
                if x < 0 or x >= m or y < 0 or y >= n or (x, y) in visited or board[x][y] not in root.kids: continue
                helper(x, y, root.kids[board[x][y]], visited, word + board[x][y])
            visited.remove((i, j))

            return        
        
        for word in words: setTrie(word)

        for i in range(m):
            for j in range(n):
                if board[i][j] in root.kids: helper(i, j, root.kids[board[i][j]], set(), board[i][j])         
                
        return list(res)