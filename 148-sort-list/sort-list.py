class Solution:
    def sortList(self, head):
        # Base case
        if not head or not head.next:
            return head

        # Find the middle
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Split the list
        mid = slow.next
        slow.next = None

        # Sort both halves
        left = self.sortList(head)
        right = self.sortList(mid)

        # Merge the sorted halves
        return self.merge(left, right)

    def merge(self, left, right):
        dummy = ListNode(0)
        tail = dummy

        while left and right:
            if left.val < right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next

            tail = tail.next

        if left:
            tail.next = left
        else:
            tail.next = right

        return dummy.next