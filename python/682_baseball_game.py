class Solution:
    def calPoints(self, operations: list[str]) -> int:
        record = []
        score = 0

        for o in operations:
            if o == '+':
                record.append(record[-1] + record[-2])
                score += record[-1]
            elif o == 'D':
                record.append(record[-1]*2)
                score += record[-1]
            elif o == 'C':
                score -= record[-1]
                record.pop(-1)
            else:
                record.append(int(o))
                score += record[-1]

        return score   

class Solution2:
    def calPoints(self, ops: list[str]) -> int:
        record = []

        for o in ops:
            if o == '+':
                record.append(record[-1] + record[-2])
            elif o == 'D':
                record.append(record[-1]*2)
            elif o == 'C':
                record.pop(-1)
            else:
                record.append(int(o))

        return sum(record)       

# test
tests = [ 
    (["5","2","C","D","+"],                 30),
    (["5","-2","4","C","D","9","+","+"],    27),
    (["1","C"],                             0),
]

for ops,solution in tests:
    sol = Solution2()
    sol = sol.calPoints(ops)
    print( sol == solution )