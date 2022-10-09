class NeetSolution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda pair: pair[0])
        output = [intervals[0]]

        for start, end in intervals:
            lastEnd = output[-1][1]

            if start <= lastEnd:
                # merge
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])
        return output

# tests
tests = [ 
    (
        [[1,3],[2,6],[8,10],[15,18]],
        [[1,6],[8,10],[15,18]]
    ),
    (
        [[1,4],[4,5]],
        [[1,5]]
    ),
]

for intervals, solution in tests:
    sol = NeetSolution()
    sol = sol.merge(intervals)
    print( sol == solution )