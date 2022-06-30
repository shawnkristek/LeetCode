from collections import defaultdict

class Solution:
    def topKFrequent(nums: list[int], k: int) -> list[int]:
        hmap = defaultdict(int)
        output = [-1] * k
        
        # count all nums
        for num in nums:
            hmap[num] += 1
        
        # sort counts
        sorted_map = sorted(hmap.items(), key=lambda item: item[1], reverse=True)
        
        # output top k counts as list
        for i in range(k):
            output[i] = sorted_map[i][0]
        
        return output

class Solution1:
    def topKFrequent(nums: list[int], k: int) -> list[int]:
        # initialize dictionary, one that will create an entry if one is not present
        counts = defaultdict(int)
        # init list of len(nums) empty lists
        freq = [[] for i in range(len(nums)+1)]

        # count all nums
        for num in nums:
            counts[num] += 1

        # sort counts by appending each num to freq[count]
        for num, count in counts.items():
            freq[count].append(num)

        output = []
        # pop k nums from freq starting at tail end
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                output.append(n)
                if len(output) == k:
                    return output
        # return []

# test
# nums = [1,1,1,2,2,3]
nums = [1]
k = 1
print(Solution1.topKFrequent(nums, k))