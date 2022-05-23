#kadane algorithm
#problem link - https://leetcode.com/problems/max-consecutive-ones/
#finding max consecutive numbers

class Solution:
    def findMaxConsecutiveOnes(self, nums: "list[int]") -> int:

        loc_max = glo_max = 0
        for i in range(len(nums)):
            if nums[i] == 1: 
                loc_max += 1
            elif nums[i] != 1:
                glo_max = max(glo_max, loc_max)
                loc_max = 0  
        #in case of the corner case [.....,1 ,1, 1]         
        return max(glo_max, loc_max)