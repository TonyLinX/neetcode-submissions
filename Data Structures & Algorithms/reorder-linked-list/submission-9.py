# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        這題就是 reorder linklist 符合: [0, n-1, 1, n-2, 2, n-3, ...]
        * 想法: 使用快慢指標找出中間點。 切成兩個 list1 and list2，但是需要反轉 list2。
                按照 list1->list2->list1->list2....持續接完。
        * 當時的犯錯: 少想了 list2 需要反轉
        """
        #找中間點
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 

        list2 = slow.next
        slow.next = None

        # 反轉
        prev = None

        while list2:
            nxt = list2.next
            list2.next = prev
            prev = list2
            list2 = nxt
        
        list2 = prev
        # merge 
        dummy = ListNode(-1)
        curr = dummy
        list1 = head
        while list1 and list2:
            nxt1 = list1.next
            nxt2 = list2.next
            curr.next = list1
            curr = list1
            curr.next = list2
            curr = list2
            list1 = nxt1
            list2 = nxt2

        curr.next = list1 if list1 else list2
