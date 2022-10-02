class Solution:
    def isHappy(self, n: int) -> bool:
        
        def sumSqs(num: int):
            return sum([(int(digit) ** 2 ) for digit in str(num)])

        totals = [n] # use hash set instead
        total = sumSqs(n)

        while total != 1:
            if total in totals: 
                return False

            totals.append(total)
            total = sumSqs(total)

        return True


class NeetSolution:
    def isHappy(self, n: int) -> bool:
        slow, fast = n, self.sumSquareDigits(n)

        while slow != fast:
            fast = self.sumSquareDigits(fast)
            fast = self.sumSquareDigits(fast)
            slow = self.sumSquareDigits(slow)
            print(slow,fast)

        return True if fast == 1 else False

    def sumSquareDigits(self, n):
        output = 0
        while n:
            output += (n % 10) ** 2
            n = n // 10
        return output

# test

tests = [ 
    ( 19, True),
    ( 2,  False),
    ( 985357299239,  False),
]

for n,solution in tests:
    sol = NeetSolution()
    sol = sol.isHappy(n)
    print( sol == solution )