class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[list[int]]:
        res = []
        M,N = len(matrix[0]), len(matrix)
        m,n = 0,0
        c,r = 0,0

        while len(res) < len(matrix[0]) * len(matrix):
            for c in range(m,M):
                res.append(matrix[r][c])
            n += 1
            for r in range(n,N):
                res.append(matrix[r][c])
            M -= 1
            for c in reversed(range(m,M)):
                res.append(matrix[r][c])
            N -= 1
            for r in reversed(range(n,N)):
                res.append(matrix[r][c])
            m += 1
    
        return res[: len(matrix[0]) * len(matrix)]
        
# test

tests = [
    (
        [[1,2,3],[4,5,6],[7,8,9]],
        [1,2,3,6,9,8,7,4,5]
    ),
    (
        [[1,2,3,4],[5,6,7,8],[9,10,11,12]],
        [1,2,3,4,8,12,11,10,9,5,6,7]
    ),
]

for matrix,solution in tests:
    sol = Solution()
    sol = sol.spiralOrder(matrix)
    print( sol == solution )