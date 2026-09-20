# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)

        if k == 0:
            return None
        elif k == 1:
            return lists[0]

        while len(lists) > 1:
            mergeLists = []
            for i in range(0, len(lists), 2): # 0 2 4 6 8
                l1 = lists[i]
                l2 = lists[i+1] if i != len(lists)-1 else None
                mergeLists.append(self.mergeTwoList(l1,l2))
            lists = mergeLists

        return lists[0]
    def mergeTwoList(self, list1: Optional[ListNode],list2: Optional[ListNode]) -> Optional[ListNode]:

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

        curr.next = list1 if list1 else list2
            
    
        return dummy.next
        
        