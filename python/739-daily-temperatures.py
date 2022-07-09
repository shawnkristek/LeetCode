class Solution:
    def dailyTemperatures(temperatures: list[int]) -> list[int]:
        output = [0] * len(temperatures)
        stack = []
        
        for i,t in enumerate(temperatures):
            # check ea stack element against current temp
            while stack and stack[-1][1] < t:
                sIndx, sTemp = stack.pop()
                # update output if greater
                output[sIndx] = i - sIndx
            
            # push index,temp to stack
            stack.append([i,t])
            
        return output

# test
tests = [
([73,74,75,71,69,72,76,73], [1,1,4,2,1,1,0,0]),
([30,40,50,60], [1,1,1,0]),
([30,60,90], [1,1,0])
]

for temperatures,solution in tests:
    print(Solution.dailyTemperatures(temperatures) == solution)