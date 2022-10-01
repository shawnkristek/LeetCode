class Solution:
    def twoSum(nums: list[int], target: int) -> list[int]:
        # store previously seen values
        prevMap = {} # val -> index
        
        # loop thru elements checking if target - num has been seen
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                # once solution found, return indicies 
                return [prevMap[diff], i]
            # not found? add element to seen values
            prevMap[n] = i

        # every input has one solution
        #return []

#test
nums = [2,7,11,15]
target = 9

print(Solution.twoSum(nums, target))