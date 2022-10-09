from reuse import TreeNode
from collections import deque

class NeetSolution:
    def rightSideView(self, root: TreeNode) -> list[int]:
        res = []
        q = deque([root])

        while q:
            rightSide = None
            qLen = len(q)

            for i in range(qLen):
                node = q.popleft()
                if node:
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)
            
            if rightSide:
                res.append(rightSide.val)

        return res

# test
tests = [ 
    (TreeNode().build([1,2,3,None,5,None,4]),       [1,3,4]),
    (TreeNode().build([1,None,3]),                  [1,3]),
    (TreeNode().build([]),                          []),
]

for root,solution in tests:
    sol = NeetSolution()
    sol = sol.rightSideView(root)
    print ( sol == solution )