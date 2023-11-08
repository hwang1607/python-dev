# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #find middle
        slow = head
        fast = head

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        #need node before second half to split list
        second = slow.next
        slow.next = None
        prev = None

        while second: 
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        temphead = head
        while prev: #shorter if odd
            temp1 = temphead.next
            temp2 = prev.next
            
            temphead.next = prev
            prev.next = temp1

            temphead = temp1
            prev = temp2

            


        