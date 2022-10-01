from reuse import TreeNode

class NeetSolution:
    def isBalanced(self, root: TreeNode) -> bool:

        def dfs(root: TreeNode) -> list[bool,int]:
            if root is None:
                return [True, 0] 

            left, right = dfs(root.left), dfs(root.right)
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1

            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]

# class Solution:
#     def __init__(self):
#         self.balanced = True

#     def isBalanced(self, root: TreeNode) -> bool:
    
#         def dfs(self, root: TreeNode) -> int:
#             if root is None:
#                 return 0
    
#             left = self.dfs(root.left)
#             right = self.dfs(root.right)
    
#             self.balanced = self.balanced and abs(left - right) <= 1
    
#             return 1 + max(left, right)
    
#         return self.balanced


# test
tests = [ 
    (TreeNode().build([3,9,20,None,None,15,7]),     True),
    (TreeNode().build([1,2,2,3,3,None,None,4,4]),   False),
    (TreeNode(),                                    True)
]

for root,solution in tests:
    sol = NeetSolution()
    sol = sol.isBalanced(root)
    print( sol == solution )