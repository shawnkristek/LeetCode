class Solution:
    def isValid(s: str) -> bool:
        stack = []

        for c in s:
            if c in "({[":
                stack.append(c)
                continue
            elif stack:
                popped = stack.pop()
                match c:
                    case ')':
                        if popped != '(':
                            break
                    case '}':
                        if popped != '{':
                            break
                    case ']':
                        if popped != '[':
                            break
            else:
                break
        else: # if for loop completes and stack empty 
            if not stack:
                return True
        # otherwise
        return False

class Solution1:
    def isValid(s: str) -> bool:
        map = { ")":"(", "]":"[", "}":"{"}
        stack = []

        for c in s:
            if c not in map:
                stack.append(c)
                continue
            if not stack or stack[-1] != map[c]:
                return False
            stack.pop()

        return not stack


# test
tests = [
    ("()", True),
    ("()[]{}", True),
    ("(({[]}))", True),
    ("(()){[}]", False),
    ("(]", False),
    ("[", False),
    ("]", False),
    ("", True)
]

for s,solution in tests:
    print(Solution1.isValid(s) == solution)