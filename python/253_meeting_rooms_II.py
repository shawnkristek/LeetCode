class NeetSolution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        start = sorted([i[0] for i in intervals])
        end = sorted([i[1] for i in intervals])

        res, count = 0, 0
        s, e = 0, 0
        while s < len(intervals):
            if start[s] < end[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1
            res = max(res, count)

        return res

# test

tests = [ 
    (
        [(0,30),(5,10),(15,20)],
        2
    ),
    (
        [(2,7)],
        1
    ),
]

for intervals,solution in tests:
    sol = NeetSolution()
    sol = sol.minMeetingRooms(intervals)
    print( sol == solution )