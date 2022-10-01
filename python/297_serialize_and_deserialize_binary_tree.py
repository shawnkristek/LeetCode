from reuse import TreeNode

class NeetSolution:

    def serialize(self, root: TreeNode) -> str:
        """ Encodes a tree to a single string.  """
        res = []

        def dfs(node):
            if not node:
                res.append("N")
                return

            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(res)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.  """
        vals = data.split(",")
        self.i = 0

        def dfs():
            if vals[self.i] == "N":
                self.i += 1
                return None

            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()

# test
tests = [ 
    (TreeNode().build([1,2,3,None,None,4,5])),
    (TreeNode().build([])),
]

for root in tests:
    sol = NeetSolution()
    ser = sol.serialize(root)
    res = sol.deserialize(ser)

    res = res.values() if res else res
    roo = root.values() if root else root

    print( res == roo )

