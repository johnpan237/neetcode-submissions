# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find the start of second half
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse the second half
        second = self.reverseList(slow.next)
        slow.next = None
        first = head

        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
    
    def reverseList(self, head: Optional[ListNode]) -> None:
        prev, cur = None, head

        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        
        return prev

    # Time Complexity: O(n)
    # Space Complexity: O(1)