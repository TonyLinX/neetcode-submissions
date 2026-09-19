# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        這題就是判斷 listlist 是否有 cyclee
        * 想法:
            * 可以用快慢指標，讓 slow 跑一格 fast 一次跑兩格。如果有環 fast一定會追上 slow 。
            * 從頭一個起跑線開始。
            * 結束訊號是看是否有人跑完
        """
        slow = fast = head

        while slow and fast:
            slow = slow.next
            fast = fast.next.next if fast.next != None else None
            if slow and fast and slow == fast:
                return True

        return False