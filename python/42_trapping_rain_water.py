class Solution:
    def trap(height: list[int]) -> int:
        if not height: return 0

        volume = 0
        left, right = 0, len(height)-1
        maxL, maxR = height[left], height[right]

        while left < right:
            if maxL < maxR:
                left += 1
                maxL = max(maxL, height[left])
                volume += maxL - height[left]
            else:
                right -= 1
                maxR = max(maxR, height[right])
                volume += maxR - height[right]

        return volume

# test
tests = [
    ([0,1,0,2,1,0,1,3,2,1,2,1], 6),
    ([4,2,0,3,2,5], 9),
    ([],0)
]

for height, solution in tests:
    print(Solution.trap(height) == solution)