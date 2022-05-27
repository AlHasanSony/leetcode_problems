#problem - https://leetcode.com/problems/combinations/



    
class Solution(object):
    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.res = [[]]
        self.k = k
        self._subset(n)
        return [x for x in self.res if len(x) == k]

    def _subset(self, n):
        if not n:
            return
        for r in self.res[:]:
            if len(r) < self.k:
                t = r[:]
                t.append(n)
                self.res.append(t)
        self._subset(n-1)