# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        """
        用 for loop 便利整個 list，知道 list 多長。
        然後每便利一個就去計算該點的  nth_from_tail，如果是目標點就使用 prev,curr, after  進行 remove
        * 當時的犯錯:
            * remove 如果再 remove head 的時候，需要一個 dummy head 要不然在 prev.next 可能是None出錯
              以及 remove 頭的話需要改變頭 (head = head.next)
        """
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        i = 0
        dummy = ListNode(-1)
        curr = head
        prev = dummy
        while curr:
            nth_from_tail = length - i
            if nth_from_tail == n:
                if curr == head:
                    head = head.next
                prev.next = curr.next
                curr.next = None
                break
            prev = curr
            curr = curr.next
            i += 1

            
        return head