class Greedy:
    def canJump(self, nums: list[int]) -> bool:
        goal_index = len(nums)-1
        
        for i,n in reversed(list(enumerate(nums))):
            if i + n >= goal_index:
                goal_index = i
        return goal_index == 0

# test
tests = [ 
    ([2,3,1,1,4],       True),
    ([3,2,1,0,4],       False),
]

for nums,solution in tests:
    sol = Greedy()
    sol = sol.canJump(nums)
    print( sol == solution )