from re import I


class Solution:
    def myPow(self, x: float, n: int) -> float:
        result = 1
        
        for i in range(abs(n)):
            result = result * x
        
        if n < 0:
            result = 1 / result
            
        return result

class Solution1:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        def helper(x: float, n: int) -> float:
            # end condition: n <= 3
            if n <= 3:
                res = 1
                for i in range(n):
                    res = res * x
                return res
            
            # if even n
            if n % 2 == 0:
                res = helper(x, n // 2)
                return res * res
            else: # if odd n
                res = helper(x, n // 2)
                return res * res * x

        res = helper(x,abs(n))
        if n < 0:
            res = 1 / res
        return res

class NeetSolution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            if x == 0:
                return 0
            if n == 0:
                return 1

            res = helper(x * x, n // 2)
            return x * res if n % 2 else res

        res = helper(x, abs(n))
        return res if n >= 0 else 1 / res

# test
tests = [ 
    (
        2.0, 
        10, 
        1024.0),
    (
        2.1,
        3,
        9.261000000000001
    ),
    (
        2.0,
        -2,
        0.25
    ),
    (
        0,
        0,
        0
    ),
]

for x,n,solution in tests:
    sol = Solution1()
    sol = sol.myPow(x,n)
    print( sol == solution )