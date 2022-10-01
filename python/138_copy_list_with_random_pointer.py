class Node:
    def __init__(self, x: int, next: 'Node'=None, random: 'Node'=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(head: Node) -> Node:
        oldToCopy = {None:None}

        # first pass map old nodes to copies
        curr = head
        while curr:
            copy = Node(curr.val)
            oldToCopy[curr] = copy
            curr = curr.next

        # update pointers in copy
        curr = head
        while curr:
            copy = oldToCopy[curr]
            copy.next = oldToCopy[curr.next]
            copy.random = oldToCopy[curr.random]
            curr = curr.next

        return oldToCopy[head]


# test
# tests = [
#     (),
#     (),
#     (),
# ]

# for head,solution in tests:
#     sol = Solution.copyRandomList(head)
#     print(sol == solution)