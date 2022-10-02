from reuse import TreeNode

class NeetSolution:
    def maxPathSum(self, root: TreeNode) -> int:
        res = [root.val]

        # return max path sum without split
        def dfs(root: TreeNode) -> int:
            if not root:
                return 0

            leftMax = dfs(root.left)
            rightMax = dfs(root.right)

            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            # compute max path sum WITH split
            res[0] = max(res[0], root.val + leftMax + rightMax)
            
            return root.val + max(leftMax, rightMax)

        dfs(root)

        return res[0]

# test
tests = [ 
    (TreeNode().build([1,2,3]),                     6),
    (TreeNode().build([-10,9,20,None,None,15,7]),   42),
]

for root,solution in tests:
    sol = NeetSolution()
    sol = sol.maxPathSum(root)
    print( sol == solution )