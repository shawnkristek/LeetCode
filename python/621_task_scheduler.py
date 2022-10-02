import heapq
from collections import Counter, deque

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        pass

class NeetSolution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque()

        while maxHeap or q:
            time += 1

            if not maxHeap:
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])
            
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time

# test

tests = [
    (
        ["A","A","A","B","B","B"],
        2,
        8
    ),
    (
        ["A","A","A","B","B","B"],
        0,
        6
    ),
    (
        ["A","A","A","A","A","A","B","C","D","E","F","G"],
        2,
        16
    ),
]

for tasks,n,solution in tests:
    sol = NeetSolution()
    sol = sol.leastInterval(tasks, n)
    print( sol == solution )