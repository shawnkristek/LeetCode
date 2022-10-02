class Solution:
    def search(nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l+r) // 2

            if target == nums[mid]:
                return mid

            # left array
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else: 
                    r = mid - 1
            # right array
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1

# test
tests = [ 
    ([0,1,2,3,4,5,6,7], 0, 0),
    ([7,0,1,2,3,4,5,6], 0, 1),
    ([6,7,0,1,2,3,4,5], 0, 2),
    ([5,6,7,0,1,2,3,4], 0, 3),
    ([4,5,6,7,0,1,2,3], 0, 4),
    ([3,4,5,6,7,0,1,2], 0, 5),
    ([2,3,4,5,6,7,0,1], 0, 6),
    ([1,2,3,4,5,6,7,0], 0, 7),
    ([4,5,6,7,0,1,2], 0, 4),
    ([4,5,6,7,0,1,2], 5, 1),
    ([1], 0, -1)
]

for nums,target,solution in tests:
    print(Solution.search(nums,target) == solution)