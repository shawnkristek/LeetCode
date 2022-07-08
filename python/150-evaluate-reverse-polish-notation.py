class Solution:
    def evalRPN(tokens: list[str]) -> int:
        numbers = []

        for t in tokens:
            match t:
                case "+":
                    numbers.append(numbers.pop() + numbers.pop())
                case "-":
                    num2 = numbers.pop()
                    num1 = numbers.pop()
                    numbers.append(num1 - num2)
                case "/":
                    num2 = numbers.pop()
                    num1 = numbers.pop()
                    numbers.append(int(num1 / num2))
                case "*":
                    numbers.append(numbers.pop() * numbers.pop())
                case _ :
                    numbers.append(int(t))

        return numbers.pop() 

# test
tests = [
    (["2","1","+","3","*"], 9),
    (["4","13","5","/","+"], 6),
    (["10","6","9","3","+","-11","*","/","*","17","+","5","+"], 22)
]

for tokens,solution in tests:
    print(Solution.evalRPN(tokens) == solution)