class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True

       
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next


        second = slow.next if fast else slow


        if fast: slow.next = None
        else:
 
            prev = head
            while prev.next is not slow:
                prev = prev.next
            prev.next = None

        # reverse
        def reverse(node):
            prev = None
            while node:
                nxt = node.next
                node.next = prev
                prev = node
                node = nxt
            return prev

        second = reverse(second)


        p1, p2 = head, second
        while p2:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next
        return True
