class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        result = []
        carry = 1

        for d in reversed(digits):
            sum = d + carry
            carry = sum // 10
            sum = sum % 10
            result.append(sum)

        if carry:
            result.append(carry)

        result.reverse()
        return result

class NeetSolution:
    def plusOne(self, digits: list[int]) -> list[int]:
        one = 1
        i = 0
        digits = digits[::-1]

        while one:
            if i < len(digits):
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    one = 0
            else:
                digits.append(one)
                one = 0
            i += 1
        return digits[::-1]        


# test
tests = [ 
    (
        [1,2,3],
        [1,2,4]
    ),
    (
        [4,3,2,1],
        [4,3,2,2]
    ),
    (
        [9],
        [1,0]
    ),
]

for digits,solution in tests:
    sol = NeetSolution()
    sol = sol.plusOne(digits)
    print( sol == solution )
