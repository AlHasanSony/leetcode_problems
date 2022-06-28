#problem link - https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s):
        stack=[]
        pairs = {")","(",
                 "}", "{",
                 "]", "["     
        }
        for c in s:


















# class solution:
#     def isValid(self, s) -> bool:
#         s = list(s)
#         for i in range (len(s)-1):
#             if s[i] == '(' and s[i+1]==(')'):
#                 return True
#             elif s[i] == '[' and s[i+1]==(']'):
#                 return True
#             elif s[i] == '{' and s[i+1]==('}'):
#                 return True
#             return False
#     y = "()"
#     x = isValid(1, y)
#     print(x)
        