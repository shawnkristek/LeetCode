class Solution:
    def longestConsecutive(nums: list[int]) -> int:
        # create set from nums
        numSet = set(nums)
        longest = 0
        
        # loop thru nums checking and counting consecutive elements
        for n in numSet: # corrected to search set, significant performance improvement
            if (n-1) not in numSet:
                length = 1
                while n + length in numSet:
                    length += 1
                # passing vals as list to max improved performance
                longest = max([longest, length])
                
        return longest

# test
cases = [
  ([100,4,200,1,3,2], 4),
  ([0,3,7,2,5,8,4,6,0,1], 9)
]

for case, solution in cases:
  print(Solution.longestConsecutive(case) == solution)
