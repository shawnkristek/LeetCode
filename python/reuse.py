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

    def build(self, values: list[int]): 
        '''
        Given an array of ints,
        Return a linked-list 
        '''
        next = None
        for v in reversed(values):
            next = ListNode(v, next)

        return next