class Solution:
    def myPow(self, x: float, n: int) -> float:
        result = 1
        
        for i in range(abs(n)):
            result = result * x
        
        if n < 0:
            result = 1 / result
            
        return result

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
]

for x,n,solution in tests:
    sol = Solution()
    sol = sol.myPow(x,n)
    print( sol == solution )