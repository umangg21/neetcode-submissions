# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def doReverse(head, k):
            count = 0
            tail = head
            while (count<k and tail):
                tail = tail.next
                count+=1 
            if count <k:
                return (head, None)
            # print(count, k, head.val)
                
            count = 0
            curr = head
            prev = None

            while(count <k):
                # print(count, curr.val)
                temp = curr.next
                curr.next = prev
                prev, curr = curr, temp
                count =count+1

            return (prev, curr)

        head, tail = doReverse(head, k)
        dummy1 = head
        while tail:
            next_h, next_tail = doReverse(tail, k)
            while head.next:
                head = head.next
            head.next = next_h
            tail = next_tail
            # print_linked_list(dummy1)

        return dummy1




