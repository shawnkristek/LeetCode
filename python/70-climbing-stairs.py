class Solution:
    def climbStairs(self, n: int) -> int:
        pass

# test

tests = [ 
    (
        2,
        2
    ),
    (
        3,
        3
    ),
]

for n,solution in tests:
    sol = Solution()
    sol = sol.climbStairs(n)
    print( sol == solution )