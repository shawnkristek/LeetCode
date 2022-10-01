from tkinter import N


class Solution:
    def minSubArrayLen(target: int, nums: list[int]) -> int:
        _sum = 0
        start = 0
        end = -1 
        minsize = 0

        for i in range(0, len(nums)):
            # catch easy solution of one number
            if nums[i] >= target:
                return 1
            
            # update sum and end
            _sum += nums[i]
            end = i

            # update minsize if target achieved
            if _sum >= target:
                if minsize == 0:
                    minsize = end-start+1
                else:
                    minsize = min(minsize, end-start+1)
            
            # attempt to minimize size for minsize > 2
            # by shrinking window
            while _sum > target and minsize > 2:
                _sum -= nums[start]
                start += 1
                if _sum >= target:
                    minsize = min(minsize, end-start+1)

            # print(f'{i}: sum:{_sum} count:{minsize} start:{start} end:{end}')
        return minsize 

class Solution1:
    def minSubArrayLen(target: int, nums: list[int]) -> int:
        _sum = 0
        start = 0
        minsize = len(nums)+1
        for end, n in enumerate(nums):
            _sum += n
            while _sum >= target:
                minsize = min(minsize, end-start+1)
                _sum -= nums[start]
                start += 1
        return minsize if minsize <= len(nums) else 0

# test
nums = [1,2,3,4,5]
target = 11
print(Solution1.minSubArrayLen(target, nums))