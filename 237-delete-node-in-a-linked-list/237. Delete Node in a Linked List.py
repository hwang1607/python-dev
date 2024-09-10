# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        follower = node

        node.val = node.next.val
        node = node.next

        while node:
            if node.next:
                node.val = node.next.val
            else:
                follower.next = None
            node = node.next
            follower = follower.next
        