import heapq

class NeetSolution:
    def __init__(self, k: int, nums: list[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]

# test

tests = [ 
    (
        3, [4,5,8,2],
        [(3,4),(5,5),(10,5),(9,8),(4,8)]
    ),
]

for k,nums,cases in tests:
    sol = NeetSolution(k, nums)

    for input,solution in cases:
        print( sol.add(input) == solution )