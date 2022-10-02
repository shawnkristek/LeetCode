class Solution:
    def searchMatrix(matrix: list[list[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        # binary search rows
        top, btm = 0, ROWS - 1
        while top <= btm:
            row = (top + btm) // 2

            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                btm = row - 1
            else: # if target in row
                break

        # binary search target row
        start, end = 0, COLS - 1
        while start <= end:
            mid = (start + end) // 2

            if target == matrix[row][mid]:
                return True

            if target < matrix[row][mid]:
                end = mid - 1
            else:
                start = mid + 1

        return False

# test
tests = [ 
    ([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3, True),
    ([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13, False)
]

for matrix,target,solution in tests:
    print(Solution.searchMatrix(matrix, target) == solution)