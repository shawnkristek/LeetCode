import collections

class Solution:
    def isValidSudoku(board: list[list[str]]) -> bool:
        # create col, row and square structs
        squares = collections.defaultdict(set)
        columns = collections.defaultdict(set)
        rows = collections.defaultdict(set)
                
        # loop thru board checking and adding elements:
        for r in range(9):
            for c in range(9):
                el = board[r][c]
                # skip over any "."
                if el == ".":
                    continue
                # if element already present, invalid puzzle
                if  (el in rows[r] or
                    el in columns[c] or
                    el in squares[r // 3, c // 3]):
                    return False
                # add elements
                squares[ r // 3, c // 3].add(el)
                columns[c].add(el)
                rows[r].add(el)
                
        return True

# test
boards = [
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]],

[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
]

for board in boards:
  print(Solution.isValidSudoku(board))