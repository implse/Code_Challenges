# https://leetcode.com/problems/add-two-numbers/description/

# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8

import math

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Add self in addTwoNumbers arguments in the editor on leetcode

def addTwoNumbers(l1, l2):
    result_list = ListNode(0)
    current_final = result_list
    current_nodeA = l1
    current_nodeB = l2
    carry = 0
    while current_nodeA != None or current_nodeB != None:
        if current_nodeA:
            x = current_nodeA.val
        else:
            x = 0
        if current_nodeB:
            y = current_nodeB.val
        else:
            y = 0
        sum_val = x + y + carry
        carry = math.floor(sum_val / 10)
        current_final.next = ListNode(sum_val % 10)
        current_final = current_final.next
        if current_nodeA != None:
            current_nodeA = current_nodeA.next
        if current_nodeB != None:
            current_nodeB = current_nodeB.next
    if carry > 0:
        current_final.next = ListNode(carry)
    return result_list.next
