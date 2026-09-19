# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        這題就是反轉 Linklist
        * 當時的犯錯:
            * 不熟悉 Listlist 操作
            * 看不懂 Optional[ListNode]，這代表可能是 ListNode or None

        """
        if head:
            prev, after = None, head.next
        else:
            prev, after = None, None

        while head:
            head.next = prev
            prev = head
            head = after
            if after == None:
                break
            after = after.next
            
        return prev