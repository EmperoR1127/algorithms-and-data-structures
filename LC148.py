"""
Solution
Approach 1: Divide and Conquer

Intuition
The time complexity is an typical hint of divide and conquer, plus we could utilize pointers to satisfy the space constraint.
Similar as merge sort, recursively divide the linked list into two halves until the list has at most two nodes. 
Swap the two nodes with respect to their values and return the heads, or just return the head if only one node in the list.
Combine the lists and keep track the new head using a dummy node.

However, unlike array, how can we efficiently locate the middle node in the list? We could use the two-pointer technique here.
Initialize two pointer, slow and fast, respectively, and they both point to the head of the given list.
Move fast to two nodes after its current position, if possible. In the meantime, move slow only one node along the list.
When fast reaches the end of the list, slow is in the middle of the list, since fast always moves two times of nodes compared to slow.

Restricted to the constant space complexity, we can't initialize another linked list to merge two lists, instead we can merge the second half of the list into the first half. 
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if (not head) or (not head.next): # 0 or 1 node in the list
            return head
        n = head.next
        if not n.next: # two nodes in the list
            if head.val <= n.val: # already sorted
                return head
            else:
                n.next, head.next = head, None # swap nodes
                return n
        else:
            fast, slow = head, head
            while fast.next:
                fast = fast.next
                if fast.next:
                    fast = fast.next
                else:
                    break
                slow = slow.next
            last = slow
            slow, last.next = slow.next, None # split the two lists
            first, second = self.sortList(head), self.sortList(slow) # divide the list into two halves
            f_prev = ListNode(None) # always point to the node before first
            new_head, f_prev.next = f_prev, first
            while first and second: # merge two lists
                if first.val <= second.val:
                    f_prev = first
                    first = first.next
                else: # insert second between f_prev and first
                    curr = second
                    second = second.next
                    curr.next = first
                    f_prev.next = curr
                    f_prev = f_prev.next
            if not first: # second may or may not has more nodes
                f_prev.next = second
            return new_head.next
