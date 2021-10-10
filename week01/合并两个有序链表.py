#linkfor https://leetcode-cn.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        dummyhead = ListNode()
        head = dummyhead
        while l1 != None or l2 != None:
            if l1 == None or (l2 != None and l1.val>=l2.val):
                node = ListNode(l2.val)
                head.next = node
                head = node
                l2 = l2.next
            else:
                node = ListNode(l1.val)
                head.next = node
                head = node
                l1 = l1.next
        return dummyhead.next