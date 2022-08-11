import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        pass

class Solution1:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        # build heap
        mh = [-n for n in nums]
        heapq.heapify(mh)

        for i in range(k - 1):
            heapq.heappop(mh)

        return -1 * heapq.heappop(mh)

class Solution2:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heapq.heapify(nums)

        while len(nums) > k:
            heapq.heappop(nums)

        return heapq.heappop(nums)

# test

tests = [ 
    (
        [3,2,1,5,6,4],
        2,
        5
    ),
    (
        [3,2,3,1,2,4,5,5,6],
        4,
        4
    ),
]

for nums,k,solution in tests:
    sol = Solution2()
    sol = sol.findKthLargest(nums, k)
    print( sol == solution )