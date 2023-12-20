# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        values_seen = set()
        prev = None
        curr = head

        while curr:
            if curr.val in values_seen:
                prev.next = curr.next
            else:
                values_seen.add(curr.val)
                prev = curr
            curr = curr.next

        return head