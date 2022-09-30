from reuse import TreeNode

class NeetSolution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])

        return root

# test
tests = [ 
    ([3,9,20,15,7],         [9,3,15,20,7],  TreeNode().build([3,9,20,None,None,15,7]).values()),
    ([-1],                  [-1],           TreeNode().build([-1]).values()),
]

for preorder,inorder,solution in tests:
    sol = NeetSolution()
    sol = sol.buildTree(preorder, inorder)
    sol = sol.values() if sol else sol
    print( sol == solution )