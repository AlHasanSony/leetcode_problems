
#problem link - https://leetcode.com/problems/3sum/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []
        
        for i in range(n - 2): #i is the first element
            if nums[i] > 0:  # if the first element is positive, then no need to check
                break #break the loop
            if i > 0 and nums[i] == nums[i - 1]: #if the first element is same as previous element, then no need to check
                continue #continue the loop
            j, k = i + 1, n - 1 #j is the second element and k is the last element
            while j < k:        #while j is less than k
                cur = nums[i] + nums[j] + nums[k]  #current sum
                if cur < 0: #if current sum is less than 0
                    j += 1 #increment j
                elif cur > 0: #if current sum is greater than 0
                    k -= 1   #decrement k
                else:  #if current sum is 0
                    res.append([nums[i], nums[j], nums[k]]) #append the result
                    while j + 1 < k and nums[j] == nums[j + 1]: #if j is same as j + 1, then increment j
                        j += 1 #increment j
                    while k - 1 > j and nums[k] == nums[k - 1]: #if k is same as k - 1, then decrement k
                        k -= 1 #decrement k
                    j += 1 #increment j
                    k -= 1 #decrement k
        return res #return the result