# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        temp = slow = dummy

        counter = 0

        while temp:
            temp = temp.next
            if counter > n:
                slow = slow.next
            counter += 1

        print(slow)

        slow.next = slow.next.next


        return dummy.next

        