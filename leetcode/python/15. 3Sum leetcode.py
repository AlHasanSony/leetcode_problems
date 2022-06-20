
#problem link - https://leetcode.com/problems/3sum/

class Solution:
    def threeSum(self, nums:list[int]) -> list[list[int]]:

        if not len(nums):
            return None
        ret = set()
        nums.sort() #O(Nlog(N))
        for idx, n in enumerate(nums): #O(N)
            for two in self.twoSum(nums[idx + 1:], -n): #O(N)
                    ret.add(tuple([n] + two)) #O(1)
        return list(ret) #O(N)