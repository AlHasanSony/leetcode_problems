#leetcode problem: merge two sorted arrays
#problem link: https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(nums1, m, nums2, n):
        ptr1 = m - 1 
        #pointer to the last element of the first array
        ptr2 = n - 1 
        #pointer to the last element of the second array
        while ptr1 >= 0 and ptr2 >= 0: 
            #loop to merge the two arrays
            if nums1[ptr1] >= nums2[ptr2]: 
                #if the last element of the first array is greater than the last element of the second array
                nums1[ptr1 + ptr2 + 1] = nums1[ptr1] 
                #set the last element of the first array to the last element of the first array
                ptr1 -= 1 
                #decrement the pointer to the last element of the first array
            else: 
                #if the last element of the first array is not greater than the last element of the second array
                nums1[ptr1 + ptr2 + 1] = nums2[ptr2] 
                #set the last element of the first array to the last element of the second array
                ptr2 -= 1 
                #decrement the pointer to the last element of the second array
        # all the numbers in nums1 are moved to the end
        while ptr2 >= 0: 
            #loop to add the remaining numbers from the second array
            nums1[ptr2] = nums2[ptr2] 
            #set the last element of the first array to the last element of the second array
            ptr2 -= 1 
            #decrement the pointer to the last element of the second array
        # if all the numbers in nums1 are moved to the end, numbers in nums1 are in right place