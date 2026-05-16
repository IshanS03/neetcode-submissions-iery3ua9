class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        

        rows, cols = len(grid), len(grid[0])

        islands = 0 
        def dfs(i, j):
            
            if i >= rows or j >= cols:
                return
            
            if i < 0 or j < 0:
                return 
            
            if grid[i][j] == "0":
                return

            grid[i][j] = "0"

            dfs(i+1, j)
            dfs(i, j+1)
            dfs(i-1, j)
            dfs(i, j-1)

        for a in range(rows):
            for b in range(cols):
                if grid[a][b] == "1":
                    dfs(a, b)
                    islands += 1

        return islands
