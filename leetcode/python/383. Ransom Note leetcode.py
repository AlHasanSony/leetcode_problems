#problem link - https://leetcode.com/problems/ransom-note/

from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ct_ransom = Counter(ransomNote)
        ct_magazine = Counter(magazine)
        for key in ct_ransom:
            if ct_ransom[key] > ct_magazine[key]:
                return False
        return True