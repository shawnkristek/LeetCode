from re import I


class Solution:
    def threeSum(nums: list[int]) -> list[list[int]]:
        """
        after sorting input, the two sum II method is used
        """
        output = []
        length = len(nums)

        # sort
        nums.sort()

        # loop until checking last three numbers
        for i in range(length- 2):
            # skip duplicates
            if i > 0 and nums[i] == nums[i-1]:
                continue

            # i != j != k
            j = i + 1
            k = length - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]

                if sum > 0:
                    k -= 1
                elif sum < 0:
                    j += 1
                else:
                    # append to output and reset j,k
                    output.append([nums[i], nums[j], nums[k]])
                    # next
                    j += 1
                    # skip duplicates
                    while nums[j] == nums[j-1] and j < k:
                        j += 1

        return output

# test
tests = [
    ([-1,0,1,2,-1,-4], [[-1,-1,2],[-1,0,1]]),
    ([],[]),
    ([0],[]),
    ([0,0,0,0],[[0,0,0]]),
    ([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6],[[-4,-2,6],[-4,0,4],[-4,1,3],[-4,2,2],[-2,-2,4],[-2,0,2]])
]

for nums, solution in tests:
    print(Solution.threeSum(nums) == solution)