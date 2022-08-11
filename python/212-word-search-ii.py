from reuse import Trie

class Solution:
    def __init__(self):
        self.root = Trie()
        self.board = []

    def __convertBoard(self):
        pass

    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        self.board = board
        self.__convertBoard()


        pass



# test
tests = [ 
    (
        [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],
        ["oath","pea","eat","rain"],
        ["eat", "oath"]
    ),
    (
        [["a","b"],["c","d"]],
        ["abcb"],
        []
    ),
]

for board,words,solution in tests:
    sol = Solution()
    sol = sol.findWords(board, words)
    print( sol == solution )