from collections import deque
from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans =0; directions = [[0,1], [1,0], [0,-1], [-1,0]]

        def bfs(row, col):
            q = deque()
            q.append((row, col))
            grid[row][col]='0'

            while q:
                r,c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc

                    if nr<0 or nr>=len(grid) or nc<0 or nc>=len(grid[0]) or grid[nr][nc]=='0': continue

                    grid[nr][nc]='0'
                    q.append((nr,nc))
            
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] =='1':
                    bfs(row, col)
                    ans +=1
        
        return ans