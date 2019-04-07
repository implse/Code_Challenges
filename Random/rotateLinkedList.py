# Given a linked list and a positive integer k, rotate the list to the right by k places.

# For example, given the linked list 7 -> 7 -> 3 -> 5 and k = 2, it should become 3 -> 5 -> 7 -> 7.

# Given the linked list 1 -> 2 -> 3 -> 4 -> 5 and k = 3, it should become 3 -> 4 -> 5 -> 1 -> 2.

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


def rotate_linked_list(head, k):
    fast, slow = head, head

    for _ in range(k):
        fast = fast.next

    while fast.next != None:
        slow = slow.next
        fast = fast.next

    new_head = slow.next
    fast.next = head
    slow.next = None

    return new_head

# Test : list 7 -> 7 -> 3 -> 5
l1 = Node(7)
l1.next = Node(7)
l1.next.next = Node(3)
l1.next.next.next = Node(5)

new_ll = rotate_linked_list(l1, 2)

def print_ll(n):
    while n:
        print(n.value)
        n = n.next
print_ll(new_ll)
