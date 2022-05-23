#1648.  Minimum Deletions to Make Character Frequencies Unique
#Problem link - https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/

import collections


class Solution:
    
    def minDeletions(self, s: str) -> int:
        deletions=0
        char_counts = collections.Counter(s)
        freq_set = set()
        
        for char, count in char_counts.items():
            while count > 0 and count in freq_set:
                count -= 1
                deletions += 1
            freq_set.add(count)
            
        return deletions
    
    
    
    
    
    
# class Solution:
#     def minDeletions(self, s: str) -> int:
#         cnt=collections.Counter(s)
#         result=0
#         used=set()
#         for char, freq in cnt.items():
#             while freq>0and freq in used:
#                  freq --1
#                  result +=1
#             used.add(freq)
#         return result

# time limit exceeded
