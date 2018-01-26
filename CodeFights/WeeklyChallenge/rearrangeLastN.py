# https://codefights.com/interview-practice/task/5vcioHMkhGqkaQQYt

# Given a singly linked list of integers l and a non-negative integer n,
# move the last n list nodes to the beginning of the linked list.

# For l = [1, 2, 3, 4, 5] and n = 3, the output should be
# rearrangeLastN(l, n) = [3, 4, 5, 1, 2];

# For l = [1, 2, 3, 4, 5, 6, 7] and n = 1, the output should be
# rearrangeLastN(l, n) = [7, 1, 2, 3, 4, 5, 6].

def rearrangeLastN(l, n):
    sz = size(l)
    if n == 0 or n == sz:
        return l
    index = sz - n
    current = l
    head = l
    prev = None
    split = None
    end = None
    step = 0
    while current.next != None:
        if step == index - 1:
            prev = current
            split = current.next
        current = current.next
        step += 1
    end = current
    prev.next = None
    end.next = head
    return split

def size(l):
    current = l
    size = 0
    while current != None:
        size += 1
        current = current.next
    return size
