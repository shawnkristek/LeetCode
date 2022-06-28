"""
You are given an integer array nums consisting of n elements, and an integer k.
Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

SLIDING WINDOW
"""
from regex import W


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        #initialize sum and average to 0
        sum = 0.0 

        #get initial sum and avg values
        for num in nums[0:k]:
            sum += num
            #print(f'{num}: sum = {sum}')
        avg = sum / k
        #print(f'Average = {avg}')

        # loop thru nums [ 1 : length-(k-1) ]
        # update sum and check if new avg is greater
        for i in range(1,len(nums)- (k-1) ):
            #print(f'{i}')
            sum += -nums[i-1] + nums[i-1+k]
            newavg = sum / k 
            #print(f'New avg = {newavg}')
            if newavg > avg:
                avg = newavg
        return avg

class Solution1:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # intialize sum and maxavg to first values
        sum = sum(nums[0:k])
        maxavg = sum / k

        #loop thru nums
        for i in range(1, len(nums)-(k-1)):
            sum -= nums[i-1]
            sum += nums[i+k-1]
            maxavg = max(maxavg, sum/k)
        
        return maxavg
class Solution2:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxsum = currsum = sum(nums[0:k])
        for i in range(0, len(nums)-k):
            currsum += nums[i+k] - nums[i]
            if currsum > maxsum:
                maxsum = currsum
        return maxsum / k

