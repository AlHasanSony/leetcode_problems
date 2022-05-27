#problem link - https://leetcode.com/problems/rotting-oranges/ 


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        dirs = [(-1,0),(0,1),(1,0),(0,-1)]
        fresh_set=set()
        rotten = collections.deque()
        step = 0
        for x in range(row):
            for y in range(col):
                if grid[x][y]==1:
                    fresh_set.add((x,y))
                elif grid[x][y]==2:
                    rotten.append([x,y,step])
        while rotten:
            x,y,step = rotten.popleft()
            for dx, dy in dirs:
                if 0<=x+dx<row and 0<=y+dy<col and grid[x+dx][y+dy] == 1:
                    grid[x+dx][y+dy]=2
                    fresh_set.remove((x+dx,y+dy))
                    rotten.append([x+dx,y+dy,step+1])
        return step if not fresh_set else -1
    



    
# procedure: 
# Add all fresh oranges to fresh_set and append all rotten oranges to rotten_queue.
# Use BFS to find all fresh oranges that adjacent to the current rotten orange, turn these fresh oranges to rotten and remove these from fresh_set. In the meantime, track the steps of turning.
# After we finish the turning, if there is still a fresh orange in fresh_set, return -1 otherwist return the step.
