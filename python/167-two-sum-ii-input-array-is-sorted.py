# from collections import defaultdict

class Solution:
    def twoSum(numbers: list[int], target: int) -> list[int]:
        i,j = 0, len(numbers)-1

        while i < j:
            sum = numbers[i] + numbers[j]

            if sum > target:
                j -= 1
            elif sum < target:
                i += 1
            else:
                return [i+1, j+1]

class Solution1:
    def twoSum(numbers: list[int], target: int) -> list[int]:
        hmap = {} 

        for i in range(len(numbers)):
            diff = target - numbers[i]
            if diff in hmap:
                return [hmap[diff]+1, i+1]
            hmap[numbers[i]] = i
# test
cases = [
    ([2,7,11,15], 9, [1,2]),
    ([2,3,4], 6, [1,3]),
    ([-1,0], -1, [1,2])
]

for numbers, target, solution in cases:
    print(Solution1.twoSum(numbers, target) == solution)