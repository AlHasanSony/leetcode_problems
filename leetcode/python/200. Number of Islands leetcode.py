#problem - https://leetcode.com/problems/number-of-islands/


class Solution():
    def numIslands(self, grid): 
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid: #if grid is empty return 0
            return 0
        n = len(grid) #get the length of the grid
        m = len(grid[0]) #get the length of the grid

        def dfs(i, j):
            if 0 <= i < n and 0 <= j < m and grid[i][j] == '1': #if the index is valid and the value is 1
                grid[i][j] = '0' #set the value to 0
                
                #call the dfs function for the 4 adjacent nodes
                dfs(i, j - 1) 
                dfs(i, j + 1) 
                dfs(i - 1, j) 
                dfs(i + 1, j) 
                
                return 1 
            return 0

        count = sum(dfs(i, j) for i in range(n) for j in range(m)) #iterate through the grid and call dfs on each node
        return count #return the count of islands