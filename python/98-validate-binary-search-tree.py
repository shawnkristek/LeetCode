from reuse import TreeNode

class NeetSolution:
    def isValidBST(self, root: TreeNode) -> bool:
        def valid(node: TreeNode, left: int, right: int) -> bool:
            if not node:
                return True

            if not (node.val < right and node.val > left):
                return False

            return valid(node.left, left, node.val) and valid(node.right, node.val, right)

        return valid(root, float("-inf"), float("inf"))

# test
tests = [ 
    (TreeNode().build([2,1,3]),                 True),
    (TreeNode().build([5,1,4,None,None,3,6]),   False),
    (TreeNode().build([2,2,2]),                 False),
    (TreeNode().build([5,4,6,None,None,3,7]),   False),
]

for root,solution in tests:
    sol = NeetSolution()
    sol = sol.isValidBST(root)
    print( sol == solution )