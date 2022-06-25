#problem link - https://leetcode.com/problems/n-th-tribonacci-number/

class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 1:
            return n
        elif n == 2:
            return 1
        return self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
    







# class Solution:
#     def tribonacci(self, n: int) -> int:
#         if n <= 1:
#             return n
#         elif n == 2:
#             return 1
        
#         first, second, third = 0, 1, 1
#         for _ in range(3, n+1):
#             first, second, third = second, third, first + second + third
        
#         return third


# class Solution1:
#     def tribonacci(self, n: int) -> int:
#         return self.helper(n, {0:0, 1:1, 2:1})
    
#     def helper(self, n, memo):
#         if n not in memo:
#             memo[n] = self.helper(n-1, memo) + self.helper(n-2, memo) + self.helper(n-3, memo)
#         return memo[n]

        