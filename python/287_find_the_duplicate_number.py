class NeetSolution:
    def findDuplicate(nums: list[int]) -> int:
        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow

# test
tests = [
    ([1,3,4,2,2],   2),
    ([3,1,3,4,2],   3),
    ([1,1,2,3,4,5], 1)
]

for nums,solution in tests:
    sol = NeetSolution.findDuplicate(nums)
    print(sol == solution)