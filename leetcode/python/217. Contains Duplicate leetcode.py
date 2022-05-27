#problem link -  https://leetcode.com/problems/contains-duplicate/

from ast import List

#using dictionary
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:  #O(n) time and O(n) space
        duplicates = {} #dictionary to store the duplicates
        for i in nums:
          if i in duplicates:
            return True
          else:
            duplicates[i] = True
        return False



    
#  using set


# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool: #O(n) time and O(n) space
#         s = set(nums) # set is a data structure that stores unique elements
#         if len(s) == len(nums): #if set is same as list then no duplicates
#             return False
#         else:
#             return True


