from test_performance import AlgoPerformance as ap

class Dynamic:
    def maxProduct(self, nums: list[int]) -> int:
        _max = 1
        _min = 1
        output = nums[0]
        
        for n in nums:
            tmp = _max * n
            _max = max(n * _max, n * _min, n)
            _min = min(tmp, n * _min, n)
            output = max(output, _max)
            
        return output

# test
tests = [ 
    ([2,3,-2,4],    6),
    ([-2,0,-1],     0),
    ([0,0],         0),
    ([0,1,0],       1),
]

for nums, solution in tests:
    sol = Dynamic()
    sol = sol.maxProduct(nums)
    print( sol == solution )

# scaling performance test
tests = [ 
    (list(range(0,1000))),
    (list(range(0,10000))),
    (list(range(0,100000))),
    # (list(range(0,1000000))), # exceeds time limit
]

for nums in tests:
    sol = Dynamic()
    trace = ap()
    trace.start()
    sol = sol.maxProduct(nums)
    trace.stop(mem=False)