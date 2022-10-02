class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(int(num1) * int(num2))

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # create array of len = length(num1) + length(num2)
        res = [0] * (len(num1) + len(num2))

        for i in range(len(num1)):
            for j in range(len(num2)):
                num = int(num1[-1-i]) * int(num2[-1-j])
                res[i+j] += num % 10
                if res[i+j] > 9:
                    res[i+j+1] += res[i+j] // 10
                    res[i+j] = res[i+j] % 10
                res[i+j+1] += num // 10
                if res[i+j+1] > 9:
                    res[i+j+2] += res[i+j+1] // 10
                    res[i+j+1] = res[i+j+1] % 10
        
        res.reverse()
        i = 0
        while res[i] == 0 and i < len(res) - 1:
            i += 1
        res = res[i:]
        res = [str(d) for d in res]
        return "".join(res)


class NeetSoluton:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1, num2]:
            return "0"

        res = [0] * (len(num1) + len(num2))
        num1, num2 = num1[::-1], num2[::-1]
        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                digit = int(num1[i1]) * int(num2[i2])
                res[i1 + i2] += digit
                res[i1 + i2 + 1] += res[i1 + i2] // 10
                res[i1 + i2] = res[i1 + i2] % 10

        res, beg = res[::-1], 0
        while beg < len(res) and res[beg] == 0:
            beg += 1
        res = map(str, res[beg:])
        return "".join(res)

# test

tests =[ 
    (
        "2",
        "3",
        "6"
    ),
    (
        "123",
        "456",
        "56088"
    ),
    (
        "123",
        "23",
        "2829"
    ),
    (
        '0',
        '00000',
        '0'
    )
]

for num1,num2,solution in tests:
    sol = Solution()
    sol = sol.multiply(num1,num2)
    print( sol == solution )