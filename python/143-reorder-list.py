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
    def reorderList(head: ListNode) -> None:
        # fast slow pointers to find second half of list
        slow, fast = head, head.next
        while fast:
            # slow + 1
            slow = slow.next
            # fast + 2
            for i in range(2):
                # tail reached, exit
                if not fast:
                    break
                # fast + 1
                fast = fast.next

        # reverse second half
        # slow = head of second half
        temp = curr = slow.next
        slow.next = None
        while curr:
            # save next in trimmed list
            temp = curr.next
            # point new head to previous
            curr.next = slow
            # update head var
            slow = curr
            # move to next node
            curr = temp

        # combine lists
        # head -> first half
        # slow -> second half, reversed
        curr = head
        temp = curr
        while temp.next:
            # append from tail 
            temp = temp.next
            curr.next = slow 
            slow = slow.next
            # append from first half
            if curr.next and slow:
                curr = curr.next
                curr.next = temp
                curr = curr.next

        return None

class NeetSolution:
    def reorderList(head: ListNode) -> None:
        # find middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half
        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # merge two halfs
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next 
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

# test

def buildLinkedList(values: list[int]) -> ListNode:
    next = None
    for v in reversed(values):
        next = ListNode(v, next)

    return next

tests = [ 
    (buildLinkedList([1,2,3,4]), [1,4,2,3]),
    (buildLinkedList([1,2,3,4,5]), [1,5,2,4,3]),
    (buildLinkedList([1]), [1]),
    (buildLinkedList([5,6,7,8]), [5,8,6,7])
]

for head,solution in tests:
    Solution.reorderList(head)
    print(head.values() == solution )