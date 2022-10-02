import math

# class Solution:
#     def reverse(self, x: int) -> int:
#         res = abs(x)


#         if res > pow(2,31) - 1 or res < pow(-2,31):
#             return 0

#         return res if x >= 0 else -res

class NeetSolution:
    def reverse(self, x: int) -> int:
        MAX_INT =  2147483647
        MIN_INT = -2147483648

        result =  0

        while x:
            digit = int(math.fmod(x, 10))
            x = int(x/10)

            if result > MAX_INT // 10 or (result == MAX_INT // 10 and digit >= MAX_INT % 10):
                return 0
            if result < MIN_INT // 10 or (result == MIN_INT // 10 and digit <= MIN_INT % 10):
                return 0

            result = (result * 10) + digit

        return result


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
    sol = NeetSolution()
    sol = sol.reverse(x)
    print( sol == solution )