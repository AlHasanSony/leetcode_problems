# leetcode problem link - https://leetcode.com/problems/longest-palindromic-substring/


class Solution:
    def twoSum(self, numbers, target):
        
        left = 0
        right = len(numbers) - 1
        
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1
                
        return [left + 1, right + 1]


# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:        
#         i = 0
#         j = len(numbers) - 1
        
#         while i < j:
#             if numbers[i] + numbers[j] < target:
#                 i += 1
#             elif numbers[i] + numbers[j] > target:
#                 j -= 1
#             else:
#                 return [i + 1, j + 1]   
#         return []







# Time Complexity: O(N).
# Space Complexity: O(1).