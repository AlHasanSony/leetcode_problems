#problem link - https://leetcode.com/problems/find-peak-element/

class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1; #left and right pointers
        
        while (left < right): #while left is less than right
            mid = (left + right)  >> 1 #mid point
            if nums [mid] < nums [mid + 1]: #if mid is less than mid + 1
                left = mid + 1 #left is mid + 1
            else:
                right =  mid
        return left 
            
            