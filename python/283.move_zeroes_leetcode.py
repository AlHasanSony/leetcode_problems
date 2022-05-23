#problem link - https://leetcode.com/problems/rotate-array/

# 283. Move Zeroes
# Easy

# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.

# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:

# Input: nums = [0]
# Output: [0]
 

# Constraints:

# 1 <= nums.length <= 104
# -231 <= nums[i] <= 231 - 1


class Solution:
    def moveZeroes(self, nums): 
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l, r = 0, 0 # l - left pointer, r - right pointer

        while True: # loop until all zeroes are moved to the end
            while r < len(nums) and nums[r] != 0: r += 1 # move right pointer to the first zero
            while l < len(nums) and (nums[l] == 0 or l < r): l += 1 # move left pointer to the first non-zero element
            if l == len(nums) or r == len(nums): break # if all elements are zeroes, break the loop
            nums[l], nums[r] = nums[r], nums[l] # swap the elements
            l += 1 # move left pointer to the next non-zero element
            r += 1 # move right pointer to the next zero element


