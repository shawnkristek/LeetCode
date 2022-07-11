class Solution:
    def findMin(nums: list[int]) -> int:
        # binary search looking for min
        minimum = nums[len(nums) // 2]
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            minimum = min(minimum, nums[mid])

            if nums[l] <= nums[mid]:
                # right side
                if nums[r] < nums[l]:
                    l = mid + 1
                # left side
                else:
                    r = mid - 1
            else:
                # left side
                if nums[mid] <= nums[r]:
                    r = mid - 1
                # right side
                else:
                    l = mid + 1
        
        return minimum

# test
tests = [ 
    ([3,4,5,1,2], 1),
    ([4,5,6,7,0,1,2], 0),
    ([11,13,15,17], 11),
    ([0,1,2,3,4,5,6,7], 0)
]

for nums,solution in tests:
    print(Solution.findMin(nums) == solution)