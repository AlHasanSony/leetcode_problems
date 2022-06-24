#problem link - https://leetcode.com/problems/n-th-tribonacci-number/

class Solution:
    def trifibonacci(self, n: int) -> int:
        value = [0 for x in range(n+1)]
        