class Greedy:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        start = len(gas)-1
        end = 0
        tank = gas[start] - cost[start]

        while start >= end:
            while tank < 0 and start >= end:
                start -= 1
                tank += gas[start] - cost[start]
            if start == end:
                return start
            tank += gas[end] - cost[end]
            end += 1
        return -1

# test
tests = [ 
    ([1,2,3,4,5],   [3,4,5,1,2],    3),
    ([2,3,4],       [3,4,3],        -1),
]

for gas,cost,solution in tests:
    sol = Greedy()
    sol = sol.canCompleteCircuit(gas, cost)
    print( sol == solution )