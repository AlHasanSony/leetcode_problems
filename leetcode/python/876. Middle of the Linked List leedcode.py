#problem link - https://leetcode.com/problems/middle-of-the-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
   
         slow = fast = head
         while fast and fast.next:
               slow = slow.next
               fast = fast.next.next
         return slow
    
    

    
    
# Methodology
    
# The straight forward solution is iterate the linked list to get the size, then calculate the middle point of the size if the size . After that, we iterate the linked list again and stop at the middle point and return it.

# A better solution will be using fast and slow pointers, we create two pointers called slow and fast, for each move the fast pointer will go 2 steps and the slow pointer will go 1 step, the iteration will stop until the fast pointer reach to the end then the slow pointer is pointing the node that we want to return.