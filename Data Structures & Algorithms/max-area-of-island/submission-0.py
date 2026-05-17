class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        size = 0
        maxSize = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(i, j):
            
            if i<0 or j<0:
                return 0
            
            if i>= rows or j>= cols:
                return 0 
            
            if grid[i][j] == 0:
                return 0 

            grid[i][j] = 0

            return 1 + dfs(i+1, j) + dfs(i, j+1) + dfs(i-1, j) + dfs(i, j-1)

         


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    size = dfs(i, j)
                    maxSize = max(maxSize, size)

        return maxSize