from reuse import ListNode

class Solution:
    def reverseKGroup(head: ListNode, k: int) -> ListNode:
        slow = fast = head
        # fast moves to end of group
        i = 1
        while fast and i < k:
            fast = fast.next
            i += 1

        # slow steps through reversing
        while slow != fast:
            ts = slow.next
            ts.next = slow
            slow = ts

class NeetSolution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next

            # reverse group
            prev, curr = kth.next, groupPrev.next

            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp

        return dummy.next

    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next 
            k -= 1
        return curr


# test
tests = [
    (ListNode().build([1,2,3,4,5]), 2, [2,1,4,3,5]),
    (ListNode().build([1,2,3,4,5]), 3, [3,2,1,4,5]),
]

for head,k,solution in tests:
    sol = NeetSolution().reverseKGroup(head,k)
    sol = sol.values() if sol else sol
    print( sol == solution )