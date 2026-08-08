class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])
        neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        max_level = 0
        minH = [(grid[0][0], 0, 0)]
        visited = set((0, 0))
        while minH:

            level, r, c = heapq.heappop(minH)
            max_level = max(level, max_level)

            if r == rows-1 and c == cols-1:
                return max_level

            for nei in neighbors:
                new_r = r + nei[0]
                new_c = c + nei[1]
                if new_r >= rows or new_c>= cols or new_r<0 or new_c<0:
                    continue
                elif (new_r, new_c) in visited:
                    continue
                else:
                    heapq.heappush(minH, (grid[new_r][new_c], new_r, new_c))
                    visited.add((new_r, new_c))

                



