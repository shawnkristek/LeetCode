class Greedy:
    def jump(self, nums: list[int]) -> int:
        output = 0
        left = right = farthest = 0
        
        while right < len(nums)-1:
            
            for i,n in enumerate(nums[left:right + 1]):
                farthest = max(farthest, left+i+n)

            left = right + 1
            right = farthest
            output += 1
        
        return output

# test
tests = [ 
    ([2,3,1,1,4],       2),
    ([2,3,0,1,4],       2),
]

for nums, solution in tests:
    sol = Greedy()
    sol = sol.jump(nums)
    print( sol == solution )