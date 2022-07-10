class Solution:
    def search(nums: list[int], target: int) -> int:
        # calc mid index
        mid = int(len(nums) / 2)

        if nums[mid] > target:
            start = 0
            end = mid
        elif nums[mid] < target:
            start = mid + 1
            end = len(nums)
        else:
            return mid

        for i in range(start, end):
            if nums[i] == target:
                return i
        
        return -1

class Solution1:
    def search(nums: list[int], target: int) -> int:
        # calc mid index
        mid = int(len(nums) / 2)

        # check if target <= nums[mid]
        if nums[mid] > target:
            for i in range(0, mid):
                if nums[i] == target:
                    return i
                elif nums[i] > target:
                    return -1
        else:
            for i in range(mid + 1, len(nums)):
                if nums[i] == target:
                    return i
                elif nums[i] > target:
                    return -1

class Solution2:
    def search(nums: list[int], target: int) -> int:
        # set to search all
        start, end = 0, len(nums) - 1

        while start <= end:
            # check the middle of the search window 
            mid = (end + start) // 2

            # return if found
            if target == nums[mid]:
                return mid

            # else shrink search window
            if target < nums[mid]:
                # shrink tail
                end = mid - 1
            else:
                # shrink head
                start = mid + 1

        return -1

# test
tests = [
    ([-1,0,3,5,9,12], 9, 4),
    ([-1,0,3,5,9,12], 2, -1)
]

for nums,target,solution in tests:
    print(Solution2.search(nums,target) == solution)