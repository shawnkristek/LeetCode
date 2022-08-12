class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        size = len(matrix[0]) - 1

        for j in range(0, size):
            for i in range(j, size-j):
                temp = matrix[j][i]
                temp2 = matrix[i][size - j]
                matrix[i][size - j] = temp

                temp = matrix[size - j][size - i]
                matrix[size - j][size - i] = temp2

                temp2 = matrix[size - i][j]
                matrix[size - i][j] = temp

                matrix[j][i] = temp2

        return None

class NeetSolution:
    def rotate(self, matrix: list[list[int]]) -> None:
        l, r = 0, len(matrix) - 1
        while l < r:
            for i in range(r - l):
                top, bottom = l, r

                # save the topleft
                topLeft = matrix[top][l + i]

                # move bottom left into top left
                matrix[top][l + i] = matrix[bottom - i][l]

                # move bottom right into bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i]

                # move top right into bottom right
                matrix[bottom][r - i] = matrix[top + i][r]

                # move top left into top right
                matrix[top + i][r] = topLeft
            r -= 1
            l += 1        

# test
tests = [ 
    (
        [[1,2,3],[4,5,6],[7,8,9]],
        [[7,4,1],[8,5,2],[9,6,3]],
    ),
    (
        [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]],
        [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
    ),
]

for matrix,solution in tests:
    sol = Solution()
    sol.rotate(matrix)
    print ( matrix == solution )