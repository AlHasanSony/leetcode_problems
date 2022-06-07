#problem link - https://leetcode.com/problems/intersection-of-two-arrays-ii/



import collections


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]: 
        res = [] 
        #result array
        count = collections.Counter(nums1) 
        #count the number of times each number appears in the first array
        for num in nums2: 
            #loop to get the numbers from the second array
            if count[num]>0: 
                #if the number appears in the first array
                res.append(num) 
                #add the number to the result array
                count[num]-=1 
                #decrement the number of times the number appears in the first array
        return res 
    #return the result array






#2nd approach
# import collections

# class Solution(object):
#     def intersect(self, nums1, nums2):

#         if len(nums1) > len(nums2): 
#             #if the length of the first array is greater than the length of the second array
#             return self.intersect(nums2, nums1) 
#         #recursive call to the function to get the intersection of the two arrays

#         lookup = collections.defaultdict(int) 
#         #create a default dictionary to store the number of times the number appears in the first array
#         for i in nums1: #loop to get the number of times the number appears in the first array
#             lookup[i] += 1 #increment the number of times the number appears in the first array

#         res = [] 
#         #create an empty list to store the intersection of the two arrays
#         for i in nums2: 
#             #loop to get the number of times the number appears in the second array
#             if lookup[i] > 0: 
#                 #if the number appears in the first array
#                 res += i, 
#                 #add the number to the intersection of the two arrays
#                 lookup[i] -= 1 
#                 #decrement the number of times the number appears in the first array

#         return res 

#     def intersect2(self, nums1, nums2): 

#         c = collections.Counter(nums1) & collections.Counter(nums2) 
#         #get the intersection of the two arrays
#         intersect = [] 
#         #create an empty list to store the intersection of the two arrays
#         for i in c: 
#             #loop to get the number of times the number appears in the intersection of the two arrays
#             intersect.extend([i] * c[i]) 
#             #add the number to the intersection of the two arrays
#         return intersect 
#     #return the intersection of the two arrays