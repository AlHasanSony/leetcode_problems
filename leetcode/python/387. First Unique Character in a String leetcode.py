#problem link - https://leetcode.com/problems/first-unique-character-in-a-string/

import collections


class Solution(object):
    def firstUniqChar(self, s):

        counter = collections.Counter(s)
        
        for i, v in enumerate(s):
            if counter[v] == 1:
                return i
        
        return -1