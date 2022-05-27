#problem - https://leetcode.com/problems/merge-k-sorted-lists/





class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists or len(lists) == 0: #if list is empty or None return None
            return None
        
        while len(lists) > 1:
            mergedLists = [] #list to store the merged lists
            for i in range(0, len(lists), 2): #iterate through the list by 2s
                l1 = lists[i] #get the first list
                l2 = lists[i + 1] if (i + 1) < len(lists) else None #get the second list if it exists else None
                mergedLists.append(self.mergeList(l1, l2)) #merge the lists and append to the merged list
            lists = mergedLists #update the list to the merged list
        return lists[0] #return the merged list
    
    def mergeList(self, l1, l2):#merge two lists
        dummy = ListNode() #create a dummy node
        tail = dummy #set the tail to the dummy node
        
        while l1 and l2: #while both lists are not empty
            if l1.val < l2.val: #if the value of the first list is less than the value of the second list
                tail.next = l1 #set the next of the tail to the first list
                l1 = l1.next #move the first list to the next node
            else: #else
                tail.next = l2 #set the next of the tail to the second list
                l2 = l2.next #move the second list to the next node
            tail = tail.next #move the tail to the next node
        if l1: #if the first list is not empty
            tail.next = l1 #set the next of the tail to the first list
        if l2: #if the second list is not empty
            tail.next = l2 #set the next of the tail to the second list
        return dummy.next #return the dummy node's next node