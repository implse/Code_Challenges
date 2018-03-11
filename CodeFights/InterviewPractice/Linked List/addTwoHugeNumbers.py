# https://codefights.com/interview-practice/task/RvDFbsNC3Xn7pnQfH

# You're given 2 huge integers represented by linked lists. Each linked list element
# is a number from 0 to 9999 that represents a number with exactly 4 digits.
# The represented number might have leading zeros. Your task is to add up these
# huge integers and return the result in the same format.

class ListNode(object):
    def __init__(self, value):
        self.value = value
        self.next = None

def addTwoHugeNumbers(a, b):
    size_a = size(a)
    size_b = size(b)
    # Case : size a > size b
    if size_a > size_b:
        dif = size_a - size_b
        while dif > 0:
            new_node = ListNode(0)
            new_node.next = b
            b = new_node
            dif -= 1
    # Case : size a > size b
    if size_b > size_a:
        dif = size_b - size_a
        while dif > 0:
            new_node = ListNode(0)
            new_node.next = a
            a = new_node
            dif -= 1
    # Reverse
    rev_a = reverse(a)
    rev_b = reverse(b)
    carry = 0
    l_out = ListNode(0)
    current_out = l_out
    while rev_a != None and rev_b != None:
        sm = (rev_a.value + rev_b.value) + carry
        if sm >= 10000:
            sd = sm % 10000
            carry = 1
            current_out.next = ListNode(sd)
        else:
            current_out.next = ListNode(sm)
            carry = 0
        rev_a = rev_a.next
        rev_b = rev_b.next
        current_out = current_out.next
    if carry == 1:
        current_out.next = ListNode(carry)
    return reverse(l_out.next)

# Reverse a Linked List
def reverse(l):
    current = l
    next_node = None
    previous_node = None
    while current != None:
        next_node = current.next
        current.next = previous_node
        previous_node = current
        current = next_node
    return previous_node

# Get the size
def size(l):
    size = 0
    while l != None:
        size += 1
        l = l.next
    return size
