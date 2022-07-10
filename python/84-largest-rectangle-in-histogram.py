class Solution:
    def largestRectangleArea(heights: list[int]) -> int:
        stack = [] # index, height
        maxArea = 0

        for i,h in enumerate(heights):
            sIndx = i
            while stack and h < stack[-1][1]:
                # pop previous
                sIndx, sHeight = stack.pop(-1)

                # calc area for popped
                maxArea = max(maxArea, sHeight * (i - sIndx))

            # push newest start-index, height
            stack.append([sIndx, h])

        # calc any remaining areas
        while stack:
            sIndx, sHeight = stack.pop(-1)
            maxArea = max(maxArea, sHeight * (i - sIndx + 1))

        return maxArea

class Solution1:
    def largestRectangleArea(heights: list[int]) -> int:
        stack = [] # index, height
        maxArea = 0

        for i,h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                # pop previous
                sIndx, sHeight = stack.pop()

                # calc area for popped
                maxArea = max(maxArea, sHeight * (i - sIndx))
                start = sIndx

            # push newest start-index, height
            stack.append([start, h])

        # calc any remaining areas
        length = len(heights)
        for i,h in stack:
            maxArea = max(maxArea, h * (length - i))

        return maxArea

# test
tests = [
    ([2,1,5,6,2,3], 10),
    ([2,4,], 4)
]

for heights,solution in tests:
    print(Solution1.largestRectangleArea(heights) == solution)