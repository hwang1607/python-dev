# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #what we have here is a singly linked list with two non empty linked list representing two 
        #non negative integers - stored in reverse order, add and return sum as linked list, also in reverse order it seems

        #my first thought is to just convert the two linked lists into integers and then sum them then return the result as a linked list

        #second thought is to do basic math and use a carry variable


        dummy = ListNode()
        head = dummy
        carry = 0

        while l1 or l2 or carry:
            total = carry
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            
            carry = total // 10
            total %= 10
            
            dummy.next = ListNode(total)
            dummy = dummy.next

        
        return head.next

        








        