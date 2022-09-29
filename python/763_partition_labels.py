class Greedy:
    def partitionLabels(self, s: str) -> list[int]:
        result = []
        total_counts = {}
        partition_counts = {}
        partition_length = 0

        # count all letters in s
        for letter in s:
            total_counts[letter] = 1 + total_counts.get(letter, 0)

        for letter in s:
            partition_length += 1
            partition_counts[letter] = 1 + partition_counts.get(letter, 0)

            # delete letter from partition_counts if equal to total_counts
            if partition_counts[letter] == total_counts[letter]:
                del partition_counts[letter]

            # if parition_counts empty, parition complete
            if not partition_counts:
                result.append(partition_length)
                partition_length = 0
            
        return result

class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        result = []
        last_indexes = {letter:i for i,letter in enumerate(s)}
        partition_start = 0
        partition_end = 0

        for i,letter in enumerate(s):
            partition_end = max(last_indexes[letter], partition_end)
            if partition_end == i:
                result.append( partition_end - partition_start + 1)
                partition_start = i + 1

        return result

# test
tests = [ 
    ("ababcbacadefegdehijhklij",    [9,7,8]),
    ("eccbbbbdec",                  [10]),
]

for s,solution in tests:
    sol = Solution()
    sol = sol.partitionLabels(s)
    print( sol == solution )