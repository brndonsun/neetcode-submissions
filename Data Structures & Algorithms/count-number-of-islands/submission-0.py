class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        visited = set()

        islands = 0
        directions =[[1,0], [-1, 0], [0, 1], [0 ,-1]]
        def dfs(row, col):
            stack = []
            visited.add((r, c))
            stack.append((r,c))

            while stack:
                curr_row, curr_col = stack.pop()
                for dr, dc in directions:
                    if ((curr_row + dr) in range(rows)) and ((curr_col + dc) in range(cols)) and grid[curr_row + dr][curr_col + dc] == "1" and (curr_row + dr, curr_col + dc) not in visited:

                        stack.append((curr_row + dr, curr_col + dc))
                        visited.add((curr_row + dr, curr_col + dc))


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    dfs(r,c)
                    islands += 1

        return islands
