#problem link - https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        
        if low % 2 == 0 :
            low += 1
        if high % 2 == 0 :
            high -= 1
        return (high - low) // 2 + 1 #floor division operator //

    
    
    
    
# class Solution:
#     def countOdds(self, low: int, high: int) -> int:
        
#         if low % 2 != 0:
#             if high % 2 != 0:
#                 return (high - low) // 2 + 1
#             else:
#                 return (high - low) // 2 + 1
#         else:
#             if high % 2 != 0: 
#                 return (high - low) // 2 + 1
#             else: 
#                 return (high - low) // 2