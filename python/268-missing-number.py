class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        res = sum(nums)

        for i in range(len(nums) + 1):
            res -= i

        return -res

class NeetSolution:
    def missingNumber(self, nums: list[int]) -> int:
        res = len(nums)

        for i in range(len(nums)):
            res += i - nums[i]

        return res

# test

tests = [ 
    (
        [3,0,1],
        2
    ),
    (
        [0,1],
        2
    ),
    (
        [9,6,4,2,3,5,7,0,1],
        8
    ),
]

for nums,solution in tests:
    sol = NeetSolution()
    sol = sol.missingNumber(nums)
    print( sol == solution )