# https://codefights.com/interview-practice/task/6rE3maCQwrZS3Mm2H

# Given two singly linked lists sorted in non-decreasing order, your task is to merge them.
# In other words, return a singly linked list, also sorted in non-decreasing order,
# that contains the elements from both original lists.

class ListNode(object):
  def __init__(self, x):
    self.value = x
    self.next = None

def mergeTwoLinkedLists(l1, l2):
    list_out = ListNode(0)
    current = list_out
    while l1 != None and l2 !=None:
        if l1 != None and l2 != None:
            if l1.value == l2.value:
                current.next = ListNode(l1.value)
                current = current.next
                current.next = ListNode(l2.value)
                current = current.next
                l1 = l1.next
                l2 = l2.next
            elif l1.value > l2.value:
                current.next = ListNode(l2.value)
                l2 = l2.next
                current = current.next
            elif l2.value > l1.value:
                current.next = ListNode(l1.value)
                l1 = l1.next
                current = current.next
    while l1 != None:
        current.next = ListNode(l1.value)
        l1 = l1.next
        current = current.next
    while l2 != None:
        current.next = ListNode(l2.value)
        l2 = l2.next
        current = current.next
    return list_out.next
