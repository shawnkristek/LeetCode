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

class Solution:
    def reverseList(head: ListNode) -> ListNode:
        current, previous = head, None

        while current:
            temp = current.next
            current.next = previous
            previous = current
            current = temp

        return previous


# test

def buildLinkedList(values: list[int]) -> ListNode:
    next = None
    for v in reversed(values):
        next = ListNode(v, next)

    return next

llist1 = buildLinkedList([1,2,3,4,5])
llist2 = buildLinkedList([1,2])
llist3 = buildLinkedList([])

tests =[ 
    (llist1, [5,4,3,2,1]),
    (llist2, [2,1]),
    (llist3, None)
]

for head, solution in tests:
    sol = Solution.reverseList(head)
    print((sol.values() if sol else None) == solution)
