class Solution:
    def getSum(self, a: int, b: int) -> int:
        '''
        only works with a,b >= 0
        '''
        tmp = a
        a = a ^ b
        b = (tmp & b) << 1

        while a & b:
            tmp = a
            a = a ^ b
            b = (tmp & b) << 1

        return a | b

class NeetSolution:
    def getSum(self, a: int, b: int) -> int:
        def add(a, b):
            if not a or not b:
                return a or b

            return add(a ^ b, (a & b) << 1)
            
        if a * b < 0:
            if a > 0:
                return self.getSum(b, a)
            if add(~a, 1) == b:
                return 0
            if add(~a, 1) < b:
                return add(~add(add(~a, 1), add(~b, 1)), 1)

        return add(a, b)

# test

tests =[ 
    (
        1,
        2,
        3
    ),
    (
        2,
        3,
        5
    ),
    (
        20,
        30,
        50
    ),
    (
        -1000,
        1000,
        0
    ),
]

for a,b,solution in tests:
    sol = Solution()
    sol = sol.getSum(a, b)
    print( sol == solution )
