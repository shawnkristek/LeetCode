from math import fmod

class Solution:
    def reverse(self, x: int) -> int:
        res = abs(x)


        if res > pow(2,31) - 1 or res < pow(-2,31):
            return 0

        return res if x >= 0 else -res

# test

tests = [ 
    (
        123,
        321
    ),
    (
        -123,
        -321
    ),
    (
        120,
        21
    ),
]

for x,solution in tests:
    sol = Solution()
    sol = sol.reverse(x)
    print( sol == solution )