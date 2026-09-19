# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        slow = fast = head

        while slow and fast:
            slow = slow.next
            fast = fast.next.next if fast.next != None else None
            if slow and fast and slow == fast:
                return True

        return False