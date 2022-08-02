from reuse import TreeNode

class Solution:
    def invertTree(root: TreeNode) -> TreeNode:
        stack = [root] if root else []

        while stack:
            # grab next node for processing
            curr = stack.pop(0)

            # swap left and right
            if curr:
                tmp = curr.left
                curr.left = curr.right
                curr.right = tmp

                # add children to stack
                if curr.left:
                    stack.append(curr.left)
                if curr.right:
                    stack.append(curr.right)

        return root

class NeetSolution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        
        # swap the children
        tmp = root.left
        root.left = root.right
        root.right = tmp

        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root

# test
tests = [
    (TreeNode().build([4,2,7,1,3,6,9]),     [4,7,2,9,6,3,1]),
    (TreeNode().build([2,1,3]),             [2,3,1]),
    (TreeNode().build([1,2]),               [1,None,2]),
    (None,                  None)
]

for root,solution in tests:
    sol = NeetSolution()
    sol = sol.invertTree(root)
    sol = (sol.values()) if sol else sol
    # print(sol)
    print( sol == solution)