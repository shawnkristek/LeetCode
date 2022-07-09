class Solution:
    def carFleet(target: int, position: list[int], speed: list[int]) -> int:
        cars = [] # position, time-to-target
        for i,p in enumerate(position):
            cars.append([p, (target - p) / speed[i]])

        stack = []        
        for p,t in sorted(cars)[::-1]:
            # don't add to stack if fleet forms
            ### time-to-target < than car ahead
            if stack and t <= stack[-1][1]:
                continue

            # add car to stack
            stack.append([p,t])

        return len(stack)

# test
tests = [
    (12, [10,8,0,5,3], [2,4,1,1,3], 3),
    (10, [3], [3], 1),
    (100, [0,2,4], [4,2,1], 1)
]

for target,position,speed,solution in tests:
    print(Solution.carFleet(target,position,speed) == solution)