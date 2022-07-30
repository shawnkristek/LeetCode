from re import X
from reuse import ListNode

class Solution:
    def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
        def sumNums(l: ListNode):
            num = 0
            x = 1
            while l:
                num += x * l.val
                l = l.next
                x *= 10
            return num

        num1 = sumNums(l1)
        num2 = sumNums(l2)

        total = num1 + num2
        if total == 0:
            return ListNode()

        # determine digits in total
        x = 1
        while total / x >= 1:
            x *= 10

        # breakdown to linkedlist
        prev = None
        while x > 1:
            x = x // 10
            digit = total // x 
            total -= digit * x
            prev = ListNode(digit, prev)

        return prev

class NeetSolution:
    def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        cur = dummy

        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # new digit
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)

            # update ptrs
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next


# test
tests = [ 
    (ListNode().build([2,4,3]),         ListNode().build([5,6,4]),   [7,0,8]),
    (ListNode().build([0]),             ListNode().build([0]),       [0]),
    (ListNode().build([9,9,9,9,9,9,9]), ListNode().build([9,9,9,9]), [8,9,9,9,0,0,0,1]),
    (ListNode().build([5,6]),           ListNode().build([5,4,9]),   [0,1,0,1]),
]

for l1,l2,solution in tests:
    sol = Solution.addTwoNumbers(l1,l2)
    print(sol.values() == solution)