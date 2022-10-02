from reuse import TreeNode

class NeetSolution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if not subRoot:
            return True

        if not root:
            return False

        if self.sameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.sameTree(root.right, subRoot)

    def sameTree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s and not t:
            return True

        if s and t and s.val == t.val:
            return self.sameTree(s.left, t.left) and self.sameTree(s.right, t.right)
        
        return False

# test
root = [1,None,1,None,1,None,1,None,1,None,1,None,1,None,1,None,1,None,1,None,1,2]
subroot = [1,None,1,None,1,None,1,None,1,None,1,2]
tests = [ 
    (TreeNode().build([3,4,5,1,2]),                         TreeNode().build([4,1,2]),  True),
    (TreeNode().build([3,4,5,1,2,None,None,None,None,0]),   TreeNode().build([4,1,2]),  False),
    (TreeNode().build(root),                                TreeNode().build(subroot),  True),
]

for root,subroot,solution in tests:
    sol = NeetSolution()
    sol = sol.isSubtree(root,subroot)
    print( sol == solution )