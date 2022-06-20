# problem link -  https://leetcode.com/problems/find-all-anagrams-in-a-string/

from collections import Counter


class Solution:
    def findAnagrams(self, s:str, p: str) -> list[int]:
        result = []
        pCounter = Counter(p)
        sCounter = Counter(s[:len(p)-1])
        
        for i in range (len(p)-1, len(s)):
            sCounter[s[i]] += 1
            if sCounter == pCounter:
                result.append(i-len(p)+1)
            sCounter[s[i - len(p) + 1]] -= 1
            if sCounter [s[i - len(p) + 1]] == 0:
                del sCounter [s[i - len(p) + 1]]
        return result


# python Counter - https://www.geeksforgeeks.org/counters-in-python-set-1/
#                - https://pymotw.com/2/collections/counter.html