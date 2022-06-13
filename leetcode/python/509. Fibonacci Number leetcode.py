#problem link: https://leetcode.com/problems/fibonacci-number/


class Solution:
    def fib(self, N: int) -> int: 
        value = [0 for x in range(N+1)] 
        value[0] = 0 # 0th fibonacci number is 0
        if N>=1:   # 1st fibonacci number is 1
            value[1] = 1  # 1st fibonacci number is 1
            for x in range(2,N+1): # 2nd fibonacci number is 1
                value[x] = value[x-1]+value[x-2] # 3rd fibonacci number is 2
        return value[-1] # return the last element of the list
        
        