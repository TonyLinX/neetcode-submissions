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
            * 不會這種寫法 after = head.next if head else None
            * 使用 while head 因為 head 是我正在處裡的，當 head == None 代表就處裡完了。
            * 由於 head 終將走道 None 所以是回傳 prev
        * T O(n), M O(1) 
        * 這題也可以用遞迴解 只是 Memory complexity 不是最好，之後再學
        """

        prev = None

        while head:
            after = head.next
            head.next = prev
            prev = head
            head = after

        return prev
