from reuse import TreeNode

class NeetSolution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        curr = root

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right

# test
tests = [ 
    (TreeNode().build([3,1,4,None,2]),          1,  1),
    (TreeNode().build([5,3,6,2,4,None,None,1]), 3,  3),
]

for root,k,solution in tests:
    sol = NeetSolution()
    sol = sol.kthSmallest(root,k)
    print( sol == solution )