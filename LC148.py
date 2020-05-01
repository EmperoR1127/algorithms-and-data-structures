"""
Solution
Approach 1: Divide and Conquer

Intuition
The time complexity is a typical hint of divide and conquer, plus we could utilize pointers to satisfy the space constraint.
Similar as merge sort, We need to identify a base case and the merge procedure.
Base case: if a list has at most one node, the list is trivally sorted.
Otherwise, divide the linked list into two halves and sort the two lists using recursion. 
Merge the two lists and return the new head.

However, unlike array, how can we efficiently locate the middle node in the list? We could use the two-pointer technique here.
Initialize two pointers, slow and fast, respectively, and they both point to the head of the given list.
Traverse two nodes each time using fast and only one node using slow, if possible.
When fast reaches the end of the list, slow is in the middle of the list, since fast always traverses two times the number of 
nodes compared to slow.

Restricted to the constant space complexity, we can't initialize another linked list to merge two lists, 
instead we can merge the second half of the list into the first half. 

Complexity Analysis

Time complexity: O(nlogn). 
Similar as the merge sort. The base cases are trivally sorted. In the merge part, we need to sort two lists with 
n/2 nodes and combine n nodes together, with O(1) steps for each node. 
T(n) = 2T(n/2) + O(n), T(n) = O(nlogn) according to the master theorem.
Space complexity: O(1). Only a constant number of pointers are initialized to divide and combine the linked list.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if (not head) or (not head.next): # base case: 0 or 1 node in the list
            return head
        else:
            fast, slow = head, head
            # find the middle of the list
            while fast.next:
                fast = fast.next
                if fast.next:
                    fast = fast.next
                else:
                    break # fast reaches the end of the list
                slow = slow.next
            last = slow
            slow, last.next = slow.next, None # split the two lists
            first, second = self.sortList(head), self.sortList(slow) # divide the list into two halves
            f_prev = ListNode(None) 
            new_head = f_prev # store the new head in a dummy node
            f_prev.next = first # link f_prev to the first
            while first and second: # merge second into first
                if first.val <= second.val: # locate the node which is smaller than first.val
                    f_prev = first
                    first = first.next
                else: # insert second between f_prev and first
                    curr = second
                    second = second.next
                    curr.next = first
                    f_prev.next = curr
                    f_prev = f_prev.next # alternate f_prev for next iteration
            if not first: # when first is None, we need to merge the remaing nodes in second, if any
                f_prev.next = second # merge the remaining nodes in second
            return new_head.next 
