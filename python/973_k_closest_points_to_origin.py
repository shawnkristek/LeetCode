import heapq

class Solution:
    pass

class NeetSolution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        pts = []
        for x,y in points:
            dist = (x ** 2) + (y ** 2)
            pts.append([dist, x, y])

        heapq.heapify(pts)
        res = []
        for i in range(k):
            dist, x, y = heapq.heappop(pts)
            res.append([x, y])

        return res

# test
tests = [ 
    (
        [[1,3], [-2,2]],
        1,
        [[-2,2]]
    ),
    (
        [[3,3], [5,-1], [-2,4]],
        2,
        [[3,3], [-2,4]]
    )
]

for points,k,solution in tests:
    sol = NeetSolution()
    sol = sol.kClosest(points,k)
    print( sol == solution )