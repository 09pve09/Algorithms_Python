You are given two non-empty linked lists representing two non-negative integers
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8



Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None



class Solution(object):
    def addTwoNumbers(self, l1, l2):
"""
:type l1: ListNode
:type l2: ListNode
:rtype: ListNode

"""
#MY WAY
        s1 = s2 =  ""
        current_node_1 = l1
        current_node_2 = l2
        while current_node_1 or current_node_2:
            if current_node_1:
                s1 = str(current_node_1.val) + s1
                current_node_1 = current_node_1.next
            if current_node_2:
                s2 = str(current_node_2.val) + s2
                current_node_2 = current_node_2.next
        sum = str(int(s1) + int(s2))
        print sum
        count = len(sum) - 1
        new_node = curr_node = ListNode(sum[count])
        count -= 1
        print count
        while count >= 0:
            curr_node.next = ListNode(sum[count])
            curr_node = curr_node.next
            count -= 1
        return new_node


class Solution:
# @return a ListNode
def addTwoNumbers(self, l1, l2):
    carry = 0
    root = n = ListNode(0)
    while l1 or l2 or carry:
        v1 = v2 = 0
        if l1:
            v1 = l1.val
            l1 = l1.next
        if l2:
            v2 = l2.val
            l2 = l2.next
        sum = v1 + v2 + carry
        carry = int(sum/10)
        val = sum%10
        # carry, val = divmod(v1+v2+carry, 10)
        # divmod(6,10)
        # [0,6]

        n.next = ListNode(val)
        n = n.next
    return root.next










        e
