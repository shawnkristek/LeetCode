from tkinter import W


class Solution:
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

# test
tests = [ 
    ([-2,1,-3,4,-1,2,1,-5,4],   6),
    ([1],                       1),
    ([5,4,-1,7,8],              23),
]

for nums, solution in tests:
    sol = Solution()
    sol = sol.maxSubArray(nums)
    print( sol == solution )