class Solution:
    def findMaxAverage(nums: list[int], k: int) -> float:
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
    def findMaxAverage(nums: list[int], k: int) -> float:
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
    def findMaxAverage(nums: list[int], k: int) -> float:
        maxsum = currsum = sum(nums[0:k])
        for i in range(0, len(nums)-k):
            currsum += nums[i+k] - nums[i]
            if currsum > maxsum:
                maxsum = currsum
        return maxsum / k

class Solution3:
    def findMaxAverage(nums: list[int], k: int) -> float:
        average = []
        _sum, start = 0, 0
        for end in range(len(nums)):
            _sum += nums[end]  # add the next element

            if end >= k - 1:
                average.append(_sum / k)  # calculate the average
                _sum -= nums[start]  # subtract the element going out
                start += 1  # slide the window

        return max(average)

class Solution4:
    """BEST RESULTS.
    Similar to Solution2, just written in a way that seems more clear that all elements are checked... k:len(nums)"""
    def findMaxAverage(nums: list[int], k: int) -> float:
        maxsum = currsum = sum(nums[:k])
        for i in range(k,len(nums)):
            currsum += nums[i] - nums[i-k]
            if currsum > maxsum:
                maxsum = currsum
        return maxsum / k

# test
cases = [
    ([1,12,-5,-6,50,3], 4, 12.75),
    ([5], 1, 5.0)
]

for nums,k,solution in cases:
    print(Solution4.findMaxAverage(nums,k) == solution)