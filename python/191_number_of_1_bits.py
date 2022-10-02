class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            n &= n - 1
            res += 1
        
        return res
        
# test

tests = [ 
    (
        0b00000000000000000000000000001011,
        3
    ),
    (
        0b00000000000000000000000010000000,
        1
    ),
    (
        0b11111111111111111111111111111101,
        31
    ),
]

for n,solution in tests:
    sol = Solution()
    sol = sol.hammingWeight(n)
    print( sol == solution )