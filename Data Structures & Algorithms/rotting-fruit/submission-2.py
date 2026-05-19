class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        m = 0
        rows = len(grid)
        cols = len(grid[0])

        rotten = []
        fresh = set()
        directions = [(-1, 0), (1, 0), (0,-1), (0, 1)]
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    rotten.append((i, j, 0))
                    
                elif grid[i][j] == 1:
                    fresh.add((i, j))

        q = deque(rotten)

        while q:

            r, c, m = q.popleft()

            for dr, dc in directions:
                nr = r + dr 
                nc = c + dc

                if (nr < 0 or nc < 0 or nr >= rows or nc >= cols
                 or grid[nr][nc] != 1):
                    continue
                
                grid[nr][nc] = 2
                fresh.remove((nr, nc))
                q.append((nr, nc, m+1))
        
        if fresh:
            return -1
        else:
            return m

            

                

