class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        rows = len(grid)
        cols = len(grid[0])
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        chests = []

        for i in range(rows):
            for j in range(cols):
                if(grid[i][j] == 0):
                    chests.append((i, j, 0))

        def bfs():

            q = deque(chests)
            visited = set()

            while q:
                r, c, d = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if nr >= rows or nc >= cols or nr < 0 or nc < 0:
                        continue
                    if grid[nr][nc] == -1 or grid[nr][nc] == 0 or (nr, nc) in visited:
                        continue         
                    
                    visited.add((nr, nc))
                    q.append((nr, nc, d+1))

                    grid[nr][nc] = d+1

        bfs()
        
        
                

            
        