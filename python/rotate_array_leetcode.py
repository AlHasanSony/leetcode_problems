#problem: https://leetcode.com/problems/rotate-array/


from ast import List #import list


class Solution:
    def reverse(self,nums,l,r): 
        while l<r:
            nums[l],nums[r]=nums[r],nums[l]
            l += 1
            r -= 1
    def rotate(self,nums:List[int],k:int)->None:
        
        n=len(nums) #n is the length of the array
        k%=n # k is the number of rotations
        self.reverse(nums, 0, n-k-1) # reverse the first k elements
        self.reverse(nums, n-k, n-1) # reverse the last n-k elements
        self.reverse(nums, 0, n-1)   # reverse the whole array
                             
                             