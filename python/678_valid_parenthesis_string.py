class Greedy:
    def checkValidString(self, s: str) -> bool:
        left_min = 0
        left_max = 0

        for c in s:
            if c == '*':
                left_min = max(left_min-1, 0)
                left_max += 1
            elif c == '(':
                left_min += 1
                left_max += 1
            else: # c == ')':
                left_min = max(left_min-1, 0)
                left_max -= 1
                if left_max < 0:
                    return False

        return left_min == 0

class Solution:
    def checkValidString(self, s: str) -> bool:
        left_min, left_max = 0, 0

        for c in s:
            if c == '(':
                left_min, left_max = left_min+1, left_max+1
            elif c == ')':
                left_min, left_max = max(left_min-1, 0), left_max-1
            else:
                left_min, left_max = max(left_min-1, 0), left_max+1
            if left_max < 0:
                return False
        return left_min == 0
# test
tests = [ 
    ('()',          True),
    ('(*)',         True),
    ('(*))',        True),
    ('(*)))',       False),
    ('((*)))',      True),
    ('(((()))',     False),
    ('(((*))',      True),
    ('((((*))',     False),
    ('((((****))',  True),
    ("(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())",    False)
]

for s,solution in tests:
    sol = Greedy()
    sol = sol.checkValidString(s)
    print( sol == solution )