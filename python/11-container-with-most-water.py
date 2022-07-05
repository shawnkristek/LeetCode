class Solution:
    def maxArea(height: list[int]) -> int:
        output = 0
        i, j = 0, len(height)-1
        while i < j:
            area = min(height[i], height[j]) * (j-i)
            output = max(output, area)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        
        return output

# test
tests = [
    ([1,8,6,2,5,4,8,3,7], 49),
    ([1,1], 1),
    ([0,0], 0),
    ([],0)
]

for height, solution in tests:
    print(Solution.maxArea(height) == solution)