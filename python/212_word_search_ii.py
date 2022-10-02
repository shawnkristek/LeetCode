class Node:
    def __init__(self, end = 0):
        self.end = end
        self.kids = {}

class Solution:
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