class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def values(self):
        values = [self.val]
        next = self.next
        while next:
            values.append(next.val)
            next = next.next

        return values

    def __repr__(self):
        return str(self.values())

    def build(self, values: list[int]) -> 'ListNode':
        '''
        Given an array of ints,
        Return a linked-list 
        [n1, n2, n3] -> n1->n2->n3
        '''
        next = None
        for v in reversed(values):
            next = ListNode(v, next)

        return next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def values(self):
        values = []
        stack = [self]
        
        while stack:
            # pop next node for processing
            curr = stack.pop(0)

            if curr:
                # append node value
                values.append(curr.val)
    
                # add children to stack for processing
                if curr.left:
                    stack.append(curr.left)
                if curr.right:
                    # if right child only
                    if not curr.left:
                        stack.append(None)
                    stack.append(curr.right)
            else:
                values.append(None)


        return values

    def __repr__(self):
        return str(self.values())


    def build(self, values: list[int]) -> 'TreeNode':
        if not values:
            return None

        head = TreeNode(values.pop(0), None, None)
        stack = [head]

        while stack:
            # pop next node for updates
            curr = stack.pop(0)

            # update left,right pointers of current node
            if values:
                curr.left = TreeNode(values.pop(0), None, None)
            if values:
                curr.right = TreeNode(values.pop(0), None, None)

            # append new nodes to stack
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)

        return head