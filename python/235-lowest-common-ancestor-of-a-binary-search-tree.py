from reuse import TreeNode

class NeetSolution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        cur = root
        
        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur

# test

tests = [ 
    (TreeNode().build([6,2,8,0,4,7,9,None,None,3,5]),   TreeNode(2,None,None),  TreeNode(8,None,None),  6),
    (TreeNode().build([6,2,8,0,4,7,9,None,None,3,5]),   TreeNode(2,None,None),  TreeNode(4,None,None),  2),
    (TreeNode().build([2,1]),                           TreeNode(2,None,None),  TreeNode(1,None,None),  2),
]

for root,p,q,solution in tests:
    sol = NeetSolution()
    sol = sol.lowestCommonAncestor(root,p,q)
    sol = sol.val if sol else sol
    print( sol == solution )