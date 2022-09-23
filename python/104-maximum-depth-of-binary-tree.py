from reuse import TreeNode

class Solution:
    def maxDepth(root: TreeNode) -> int:
        pass

# test
tests = [ 
    (TreeNode().build([3,9,20,None,None,15,7]),     3),
    (TreeNode().build([1,None,2]),                  2),
]

for root,solution in tests:
    sol = Solution.maxDepth(root)
    print( sol == solution )