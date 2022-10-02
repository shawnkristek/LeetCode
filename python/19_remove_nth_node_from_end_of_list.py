from reuse import ListNode

class Solution:
    def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
        '''
        wrong solution for edge cases
        '''
        count = 1
        next = head.next
        while next:
            next = next.next
            count += 1
        
        i = 1
        node = head 
        # node = nth - 1
        while i < (count - n):
            node = node.next
            i += 1

        if count == 1:
            return None
        
        node.next = node.next.next

        return head

class Solution1:
    def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0,head)
        slow, fast = dummy, head

        # start fast at nth node (from head)
        while n > 0 and fast:
            fast = fast.next
            n -= 1

        # find nth - 1
        while fast:
            slow = slow.next
            fast = fast.next

        # delete nth
        slow.next = slow.next.next

        return dummy.next



# test

tests = [ 
    (ListNode().build([1,2,3,4,5]), 2, [1,2,3,5]),
    (ListNode().build([1,2]), 1, [1]),
    (ListNode().build([1,2]), 2, [2]),
    (ListNode().build([1]), 1, None),
]

for head,n,solution in tests:
    sol = Solution1.removeNthFromEnd(head,n) 
    print((sol.values() if sol else sol) == solution)