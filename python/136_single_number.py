class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        res = nums[0]

        for n in nums[1:]:
            res = res ^ n

        return res

class NeetSolution:
    def singleNumber(self, nums: list[int]) -> int:
        res = 0
        for n in nums:
            res = n ^ res
        return res

# test

tests = [ 
    (
        [2,2,1],
        1
    ),
    (
        [4,1,2,1,2],
        4
    ),
    (
        [1],
        1
    ),
]

for nums,solution in tests:
    sol = Solution()
    sol = sol.singleNumber(nums)
    print( sol == solution )