class NeetSolution:
    def canAttendMeetings(self, intervals: list[list[int]]) -> bool:
        # intervals.sort(key = lambda i : i.start)
        intervals.sort()

        for i in range(1, len(intervals)):
            i1 = intervals[i - 1]
            i2 = intervals[i]

            # if i1.end > i2.start:
            if i1[1] > i2[0]:
                return False

        return True


# test

tests = [ 
    (
        [[0, 30], [5, 10], [15, 20]],
        2
    ),
    (
        [[1, 18], [18, 23], [15, 29], [4, 15], [2, 11], [5, 13]],
        4
    ),
]

for intervals,solution in tests:
    sol = NeetSolution()
    sol = sol.canAttendMeetings(intervals)
    print( sol == solution )