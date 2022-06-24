#problem link - https://leetcode.com/problems/number-of-provinces/

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len (isConnected)  #
        result = 0 #
        visit = set() # set to store visited nodes
        for i in range(n):
            if i in visit :
                continue
            s = [i] # stack to store nodes
            visit.add(i) # add i to visited nodes
            result += 1 # increment result
            
            while s: # while stack is not empty
                cur = s.pop() # pop from stack
                for j in range (n): # for each node
                    if j not in visit and isConnected[cur][j] == 1: # if node is not visited and connected
                        s.append(j) # add to stack
                        visit.add(j) # add to visited nodes
        return result # return result