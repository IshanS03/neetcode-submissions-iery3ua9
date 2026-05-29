class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        visited = set()
        region = set()
        surrounded = True  # set False if region touches a border

        def dfs(i, j):
            nonlocal surrounded
            if i < 0 or j < 0 or i >= rows or j >= cols:
                return
            if (i, j) in visited or board[i][j] != "O":
                return

            visited.add((i, j))
            region.add((i, j))

            if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
                surrounded = False

            for dr, dc in directions:
                dfs(i + dr, j + dc)

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O" and (i, j) not in visited:
                    region.clear()
                    surrounded = True
                    dfs(i, j)
                    if surrounded:
                        for r, c in region:
                            board[r][c] = "X"