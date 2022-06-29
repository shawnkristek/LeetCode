class Solution:
    def containsDuplicate(nums: list[int]) -> bool:
        hashset = set()
        
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
            
        return False


# test
numbers = [
    [1,2,3,1],
    [1,2,3,4],
    [1,1,1,3,3,4,3,2,4,2],
    []
]

for nums in numbers:
    print(Solution.containsDuplicate(nums))