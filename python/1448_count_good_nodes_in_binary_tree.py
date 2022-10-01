from reuse import TreeNode

class NeetSolution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, maxVal: int) -> int:
            if not node:
                return 0

            res = 1 if node.val >= maxVal else 0
            maxVal = max(maxVal, node.val)
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)

            return res

        return dfs(root, root.val)


# test
tests = [ 
    (TreeNode().build([3,1,4,3,None,1,5]),  4),
    (TreeNode().build([3,3,None,4,2]),      3),
    (TreeNode().build([1]),                 1),
]

for root,solution in tests:
    sol = NeetSolution()
    sol = sol.goodNodes(root)
    print( sol == solution )