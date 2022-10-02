class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0b0

        for i in range(32):
            # grab right most bit
            rt = n & 0b1

            # or with result
            res = res | rt 

            # shift result
            res = res << 1

            # shift input
            n = n >> 1

        return res >> 1


class NeetSolution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(32):
            bit = (n >> i) & 1
            res = res | (bit << (31 - i))

        return res

# test

tests = [ 
    (
        0b00000010100101000001111010011100,
        0b00111001011110000010100101000000
    ),
    (
        0b11111111111111111111111111111101,
        0b10111111111111111111111111111111
    ),
]

for n,solution in tests:
    sol = Solution()
    sol = sol.reverseBits(n)
    print( sol == solution )