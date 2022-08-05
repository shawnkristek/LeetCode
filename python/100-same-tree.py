from reuse import TreeNode

class NeetSolution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        def dfs(p: TreeNode, q: TreeNode) -> bool:
            # both null
            if not p and not q:
                return True

            if p and q and p.val == q.val:
                return dfs(p.left, q.left) and dfs(p.right, q.right)

            return False

        return dfs(p, q)

# test
tests = [
    (TreeNode().build([1,2,3]), TreeNode().build([1,2,3]),    True),
    (TreeNode().build([1,2]),   TreeNode().build([1,None,2]), False),
    (TreeNode().build([1,2,1]), TreeNode().build([1,1,2]),    False),
]

for p,q,solution in tests:
    sol = NeetSolution()
    sol = sol.isSameTree(p,q)
    print( sol == solution )