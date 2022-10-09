class NeetSolution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort()
        res = 0
        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                res += 1
                prevEnd = min(end, prevEnd)
        return res

# tests
tests =[ 
    (
        [[1,2],[2,3],[3,4],[1,3]],
        1
    ),
    (
        [[1,2],[1,2],[1,2]],
        2
    ),
    (
        [[1,2],[2,3]],
        0
    ),
]

for intervals, solution in tests:
    sol = NeetSolution()
    sol = sol.eraseOverlapIntervals(intervals)
    print( sol == solution )
