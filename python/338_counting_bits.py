class Solution:
    def countBits(self, n: int) -> int:
        res = [0] * (n + 1)

        for i in range(1, n + 1):
            r = i
            while r:
                r &= r - 1
                res[i] += 1
        
        return res

class NeetSolution:
    def countBits(self, n: int) -> int:
        dp = [0] * (n + 1)
        offset = 1

        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]

        return dp
# test

tests = [ 
    (
        2,
        [0,1,1]
    ),
    (
        5,
        [0,1,1,2,1,2]
    ),
]

for n,solution in tests:
    sol = NeetSolution()
    sol = sol.countBits(n)
    print( sol == solution )