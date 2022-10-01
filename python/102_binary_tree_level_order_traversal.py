from reuse import TreeNode
from collections import deque

class NeetSolution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        res = []
        q = deque()

        if root:
            q.append(root)

        while q:
            val = []

            for i in range(len(q)):
                node = q.popleft()
                val.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            res.append(val)

        return res

# test

tests = [ 
    (TreeNode().build([3,9,20,None,None,15,7]),     [[3],[9,20],[15,7]]),
    (TreeNode().build([1]),                         [[1]]),
    (TreeNode().build([]),                          []),
]

for root,solution in tests:
    sol = NeetSolution()
    sol = sol.levelOrder(root)
    print( sol == solution )