from math import ceil

class Solution:
    def minEatingSpeed(piles: list[int], h: int) -> int:
        # if h = length of piles return max pile
        if len(piles) == h:
            return max(piles)

        # binary search from 1 to max piles
        start, end = 1, max(piles)
        k = 0

        while start <= end:
            mid = (start + end) // 2

            # calc hours to consume all bananas at rate mid
            hours = 0
            for p in piles:
                hours += ceil(p / mid)

            # if rate acceptable save and check for smaller
            if hours <= h:
                k = mid
                end = mid - 1
            # search for larger
            else:
                start = mid + 1

        return k

class Solution1:
    def minEatingSpeed(piles: list[int], h: int) -> int:
        l, r = 1, max(piles)
        k = 0
        
        while l <= r:
            m = (l + r) // 2
            
            totalTime = 0
            for p in piles:
                totalTime += ((p-1)//m) + 1

            if totalTime <= h:
                k = m
                r = m - 1
            else:
                l = m + 1

        return k

# test
tests = [ 
    ([3,6,7,11], 8, 4),
    ([30,11,23,4,20], 5, 30),
    ([30,11,23,4,20], 6, 23),
    ([312884470], 312884469, 2)
]

for piles,h,solution in tests:
    print(Solution.minEatingSpeed(piles,h) == solution)