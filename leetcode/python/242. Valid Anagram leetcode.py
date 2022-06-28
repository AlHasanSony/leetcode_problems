#problem link- https://leetcode.com/problems/valid-anagram/

class Solution:
    def isAnagram(self, s, t):
        a = Counter(s)
        b = Counter(t)
        return a==b
    
    
    
# class Solution:
#     def isAnagram(self, s, t) -> bool:
#         return sorted(s) == sorted(t)
    
        