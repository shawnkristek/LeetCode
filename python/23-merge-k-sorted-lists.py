from reuse import ListNode

class Solution:
    def mergeKLists(lists: list[ListNode]) -> ListNode:
        def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
            tail = dummy = ListNode()
            while list1 and list2:
                if list1.val < list2.val:
                    tail.next = list1
                    list1 = list1.next
                else:
                    tail.next = list2
                    list2 = list2.next
                tail = tail.next
            if list1:
                tail.next = list1
            elif list2:
                tail.next = list2
            return dummy.next 

        output = None
        for l in lists:
            output = mergeTwoLists(output, l)

        return output

class NeetSolution:
    def mergeList(self, l1, l2):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return dummy.next    
        
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedLists.append(self.mergeList(l1, l2))
            lists = mergedLists
        return lists[0]


# test
tests = [
    ([ ListNode().build([1,4,5]), ListNode().build([1,3,4]), ListNode().build([2,6]) ],   [1,1,2,3,4,4,5,6]),
    ([],                                                                                  None),
    ([None],                                                                              None),
]

for lists, solution in tests:
    sol = NeetSolution()
    sol = sol.mergeKLists(lists)
    sol = sol.values() if sol else sol
    print( sol == solution )
