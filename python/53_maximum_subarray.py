from test_performance import AlgoPerformance as ap

class Brute:
    def maxSubArray(self, nums: list[int]) -> int:
        """
        Time complexity: O(n^2)
        Space complexity: 
        """
        # start with first element
        left = 0
        right = 0
        current_sum = nums[0]
        max_sum = nums[0]
        # max_sub = nums[left:right]
        
        while right < len(nums)-1:
            right += 1
            current_sum += nums[right]

            # test if shrinking window increases sum
            i = left
            test_sum = current_sum
            while i < right:
                test_sum -= nums[i]
                i += 1
                if test_sum > current_sum:
                    left = i 
                    current_sum = test_sum
                
            if current_sum > max_sum:
                max_sum = current_sum
                # max_sub = nums[left:right]
                
        return max_sum

class Greedy:
    def maxSubArray(self, nums: list[int]) -> int:
        n = len(nums)
        max_sum_ending_curr_index = max_sum = nums[0]
        for i in range(1, n):
            max_sum_ending_curr_index = max(max_sum_ending_curr_index + nums[i], nums[i])
            max_sum = max(max_sum_ending_curr_index, max_sum)
            
        return max_sum

# test
tests = [ 
    ([-2,1,-3,4,-1,2,1,-5,4],   6),
    ([1],                       1),
    ([5,4,-1,7,8],              23),
]


for nums, solution in tests:
    sol = Greedy()
    sol = sol.maxSubArray(nums)
    print( sol == solution )

tests = [ 
    (list(range(0,1000))),
    (list(range(0,10000))),
    (list(range(0,100000))),
]

if True:
    for nums in tests:
        sol = Dynamic()
        trace = ap()
        trace.start()
        sol = sol.maxSubArray(nums)
        trace.stop(mem=False)