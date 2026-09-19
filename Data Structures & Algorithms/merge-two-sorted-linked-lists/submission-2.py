# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        """
        這一題就是由小到大合併兩個 linklist
        * 想法:
            * 創一個 dummy head ，合併完後，就會傳 dummy.next
            * 使用一個 curr 指向排序完的 listlist 尾巴，用來操作下一個接誰的動作
            * 使用 while list1 and list2 當有人排完了就結束，但後面需要收尾剩下的那個 list
        """

        dummy = ListNode(-1)
        curr = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                curr = list1
                list1 = list1.next
            else:
                curr.next = list2
                curr = list2
                list2 = list2.next
        # 收尾
        if list1:
            curr.next = list1
        elif list2:
            curr.next = list2
             
        return dummy.next