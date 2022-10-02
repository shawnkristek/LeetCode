class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        rows, cols = [],[]
        ROWS, COLS = range(len(matrix)), range(len(matrix[0]))

        # record locations of zeroes
        for r in ROWS:
            for c in COLS:
                if matrix[r][c] == 0:
                    rows.append(r)
                    cols.append(c)

        # update matrix
        for r in rows:
            for c in COLS:
                matrix[r][c] = 0
        
        for c in cols:
            for r in ROWS:
                matrix[r][c] = 0

        return None

class NeetSolution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        # O(1)
        ROWS, COLS = len(matrix), len(matrix[0])
        rowZero = False

        # determine which rows/cols need to be zero
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZero = True

        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0

        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0

# test

tests = [ 
    (
        [[1,1,1],[1,0,1],[1,1,1]],
        [[1,0,1],[0,0,0],[1,0,1]]
    ),
    (
        [[0,1,2,0],[3,4,5,2],[1,3,1,5]],
        [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
    ),
]

for matrix,solution in tests:
    sol = Solution()
    sol.setZeroes(matrix)
    print( matrix == solution )