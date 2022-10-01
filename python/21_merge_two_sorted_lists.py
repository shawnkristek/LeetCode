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
    def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
        tail = head = ListNode()

        while list1 and list2:
            # list1.val <
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            # list2.val <
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        # list1 has more nodes
        if list1:
            tail.next = list1
        # list2 has more nodes
        elif list2:
            tail.next = list2

        return head.next 

# test

def buildLinkedList(values: list[int]) -> ListNode:
    next = None
    for v in reversed(values):
        next = ListNode(v, next)
    return next

tests = [ 
    (buildLinkedList([1,2,4]), buildLinkedList([1,3,4]), [1,1,2,3,4,4]),
    (buildLinkedList([]), buildLinkedList([]), None),
    (buildLinkedList([]), buildLinkedList([0]), [0])
]

for list1,list2,solution in tests:
    sol = Solution.mergeTwoLists(list1,list2)
    print((sol.values() if sol else sol) == solution)