from reuse import TreeNode
from collections import deque

class DFS: # recursive DFS
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        depth = 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        return depth

class DFS2: # iterative DFS
    def maxDepth(self, root: TreeNode) -> int:
        stack = [[root, 1]]
        res = 0

        while stack:
            node, depth = stack.pop()

            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return res

class BFS:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        level = 0
        q = deque([root])
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level

# test
tests = [ 
    (TreeNode().build([3,9,20,None,None,15,7]), 3),
    (TreeNode().build([1,None,2]),              2),
]

for root,solution in tests:
    sol = DFS()
    sol = sol.maxDepth(root)
    print( sol == solution )