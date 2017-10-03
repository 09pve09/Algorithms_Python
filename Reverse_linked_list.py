# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current = head
        temp = []
        while current != None:
            temp.append(current.val)
            current = current.next
        current = head
        i = len(temp) - 1
        while current != None:
            current.val = temp[i]
            current = current.next
            i -= 1
        return head
