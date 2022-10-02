from collections import Counter
class DetectSquares:

    def __init__(self):
        self.points_count = Counter()

    def add(self, point: list[int]) -> None:
        self.points_count[ tuple(point) ] += 1

    def count(self, point: list[int]) -> int:
        result = 0
        px, py = point
        for (x, y),count in self.points_count.items():
            if (abs(py - y) != abs(px - x)) or x == px or y == py:
                continue
            result += count * self.points_count[(x, py)] * self.points_count[(px, y)]
        return result

# test
ds = DetectSquares()

ds.add([3,10])
ds.add([11,2])
ds.add([3,2])

sol = ds.count([11,10])
print( sol == 1 )
sol = ds.count([14,8])
print( sol == 0 )

ds.add([11,2])

sol = ds.count([11,10])
print( sol == 2 )