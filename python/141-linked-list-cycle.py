from regex import W
from reuse import ListNode

class Solution:
    def hasCycle(head: ListNode) -> bool:
        # if not head: return False
        
        slow = fast = head #, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False

# test
n1 = ListNode(3,None)
n2 = ListNode(2,None)
n3 = ListNode(0,None)
n4 = ListNode(-4,None)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n2

list1 = n1

n1 = ListNode(1,None)
n2 = ListNode(2,None)
n1.next = n2
n2.next = n1

list2 = n1

list3 = ListNode(1,None)

tests = [ 
    (list1,  1,  True),
    (list2,  0,  True),
    (list3, -1,  False),
    (None,  -1,  False)
]

for head,pos,solution in tests:
    sol = Solution.hasCycle(head)
    print(sol == solution)