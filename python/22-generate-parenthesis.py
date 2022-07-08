class Solution:
  def generateParenthesis(n: int) -> list[str]:
    stack = []
    output = []

    def backtrack(openN: int, closedN: int):
    # openN = closedN = n
      if openN == closedN == n:
        output.append("".join(stack))
        return
    # openN < n
      if openN < n:
        stack.append("(")
        backtrack(openN + 1, closedN)
        stack.pop()
    # closedN < openN  
      if closedN < openN:
        stack.append(")")
        backtrack(openN, closedN + 1)
        stack.pop()

    backtrack(0,0)

    return output


# test
tests = [
  (3, ["((()))","(()())","(())()","()(())","()()()"]),
  (1, ["()"])
]

for n,solution in tests:
  print(Solution.generateParenthesis(n) == solution)