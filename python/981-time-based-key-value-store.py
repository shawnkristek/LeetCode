class TimeMap:
    def __init__(self):
        self.map = {} 

    def __repr__(self):
        return str(self.map)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []

        self.map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        output = ""
        values = self.map.get(key, [])
        l = 0
        r = len(values) - 1

        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                output = values[m][0]
                l = m + 1
            else:
                r = m - 1

        return output

# test

timemap = TimeMap()
print(timemap, {})
timemap.set("foo", "bar", 1)
print(timemap)
print(timemap.get("foo", 1))
print(timemap.get("foo", 3))
timemap.set("foo", "bar2", 4)
print(timemap)
print(timemap.get("foo", 4))
print(timemap.get("foo", 5))
print(timemap.get("foo", 3))

timemap = TimeMap()
print(timemap)
print(timemap.set('love','high',10))
print(timemap.set('love','low',20))
print(timemap.get('love',5))
print(timemap.get('love',10))
print(timemap.get('love',15))
print(timemap.get('love',20))
print(timemap.get('love',25))