from reuse import TreeNode

class NeetSolution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        res = [0]

        def dfs(root: TreeNode):
            if not root:
                return -1

            left, right = dfs(root.left), dfs(root.right)
            res[0] = max(res[0], 2 + left + right)

            return 1 + max(left, right)

        dfs(root)
        return res[0]

class Solution1:
    def __init__(self):
        self.max = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:

        def traverse(root: TreeNode):
            if root is None:
                return 0
            
            left, right = traverse(root.left), traverse(root.right)
            self.max = max(self.max, left + right)

            return max(left, right) + 1

        traverse(root)
        return self.max

# test
tests=[ 
    (TreeNode().build([1,2,3,4,5]),     3),
    (TreeNode().build([1,2]),           1),
]

for root,solution in tests:
    sol = Solution1()
    sol = sol.diameterOfBinaryTree(root)
    print( sol == solution )