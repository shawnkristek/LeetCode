from collections import deque

class Solution:
    def maxSlidingWindow(nums: list[int], k: int) -> list[int]:
        if not nums or k == 0: return []
        maxWindow = []

        for left in range(len(nums) - k + 1):
            right = left + k
            maxWindow.append(max(nums[left:right]))
            left += 1

        return maxWindow

# does not work
# class Solution1:
#     def maxSlidingWindow(nums: list[int], k: int) -> list[int]:
#         if not nums or k <= 0: return []
#         lastMax = max(nums[0:k])
#         maxWindow = [lastMax]

#         for i in range(k, len(nums)):
#             lastMax = max(lastMax, nums[i])
#             maxWindow.append(lastMax)

#         return maxWindow

class Solution2:
    def maxSlidingWindow(nums: list[int], k: int) -> list[int]:
        output = []
        q = deque() # index
        left = right = 0

        while right < len(nums):
            # pop smaller values from q
            while q and nums[q[-1]] < nums[right]:
                q.pop()
            q.append(right)

            # remove left val from window
            if left > q[0]:
                q.popleft()

            if (right + 1) >= k:
                output.append(nums[q[0]])
                left += 1
            
            right += 1
        
        return output


# test
tests = [
    ([1,3,-1,-3,5,3,6,7], 3, [3,3,5,5,6,7]),
    ([1], 1, [1]),
    ([3,1,1,4,5,6,7], 3, [3,4,5,6,7]),
    ([3,1,1,2,5,6,7], 3, [3,2,5,6,7]),
    ([8,7,6,9], 2, [8,7,9])
]

for nums,k,solution in tests:
    print(Solution2.maxSlidingWindow(nums,k) == solution)