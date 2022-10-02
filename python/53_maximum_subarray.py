class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        n = len(nums)
        max_sum_ending_curr_index = max_sum = nums[0]
        for i in range(1, n):
            max_sum_ending_curr_index = max(max_sum_ending_curr_index + nums[i], nums[i])
            max_sum = max(max_sum_ending_curr_index, max_sum)
            
        return max_sum

class Solution2:
    def maxSubArray(self, nums: list[int]) -> int:
        current_sum = 0
        max_sum = float('-inf')
        
        for n in nums:
            if current_sum < 0:
                current_sum = 0
            current_sum += n
            max_sum = max(max_sum, current_sum)
            
        return max_sum

class Solution3:
    def maxSubArray(self, nums: list[int]) -> int:
        current_sum = 0
        max_sum = nums[0]
        
        for n in nums:
            if current_sum < 0:
                current_sum = 0
            current_sum += n
            max_sum = max(max_sum, current_sum)
            
        return max_sum

# test
tests = [ 
    ([-2,1,-3,4,-1,2,1,-5,4],   6),
    ([1],                       1),
    ([5,4,-1,7,8],              23),
]

for nums,solution in tests:
    sol = Solution3()
    sol = sol.maxSubArray(nums)
    print( sol == solution )