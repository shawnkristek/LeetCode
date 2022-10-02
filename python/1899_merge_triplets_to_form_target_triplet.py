class Greedy:
    def mergeTriplets(self, triplets: list[list[int]], target: list[int]) -> bool:

        possible = [False] * 3

        for triplet in triplets:
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                continue

            for i in range(3):
                if triplet[i] == target[i]:
                    possible[i] = True

        return possible[0] and possible[1] and possible[2]





# test
tests = [ 
    ([[2,5,3],[1,8,4],[1,7,5]],             [2,7,5],    True),
    ([[3,4,5],[4,5,6]],                     [3,2,5],    False),
    ([[2,5,3],[2,3,4],[1,2,5],[5,2,3]],     [5,5,5],    True),
]

for triplets,target,solution in tests:
    sol = Greedy()
    sol = sol.mergeTriplets(triplets, target)
    print( sol == solution )