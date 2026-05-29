class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        rows, cols = len(heights), len(heights[0])

        pacific = set()
        atlantic = set()

        resPac = set()
        resAtl = set()

        for i in range(cols):
            pacific.add((0, i))
            atlantic.add((rows-1, i))
        
        for i in range(rows):
            pacific.add((i, 0))
            atlantic.add((i, cols-1))
            

        def dfs(i, j, val, ocean):

            if i < 0 or j < 0 or i >= rows or j >= cols:
                return 

            curVal = heights[i][j]
            
            if (curVal >= val) and ((i, j) not in ocean):
                ocean.add((i, j))
            else:
                return

            for dr, dc in directions:
                dfs(i+dr, j+dc, curVal, ocean)
        

        for row, col in pacific:
            dfs(row, col, heights[row][col], resPac)

        for row, col in atlantic: 
            dfs(row, col, heights[row][col], resAtl)

        return list(resPac.intersection(resAtl))

