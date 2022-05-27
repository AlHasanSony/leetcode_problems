#problem link- https://leetcode.com/problems/remove-nth-node-from-end-of-list/



# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # slow and fast pointers
        slow = head
        fast = head
        
        #move fast pointer n steps ahead
        for i in range(0,n):
            if fast.next is None: 
                #if n is equal to the number of nodes in the list, then delete  the head node
                if i  == n - 1:
                    head = head.next
                return head
            fast =  fast.next
        #loop untill fast node reaches  to the end 
        # Now  we will  move both slow and fast pointers
        while fast.next is not None:
            slow =  slow.next
            fast =  fast.next
        #slow pointer is pointing to the node before the node we want to delete
        #Delink the nth node from the last        
        if slow.next is not None :
            slow.next  =  slow.next.next
        return head
            
                    
        
        
        
        
        


# Time Complexity
# We are traversing the list only once, hence the time complexity is O(n), where n is the number of nodes in the list.

# Space Complexity
# We are not using any data structure for intermediate calculation, hence the space complexity will be O(1).

#Explanation

# Initialize two pointers slow and fast, pointing to the head of the linked list.
# Move fast pointer n steps ahead.
# Now, move both slow and fast one step at a time unless fast reaches to the end. The fast pointer will definitely reach to the end before slow because it is ahead.
# When we fast pointer reaches to the end, the slow pointer will be n steps behind it i.e., n steps behind the end of the list.
# At that point, we will remove the node and link it to the next of current node.
# Thus, we only have to traverse the list only once which is more efficient.