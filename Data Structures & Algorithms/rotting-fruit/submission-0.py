from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #intuition: start from every rotten fruit, bfs from there 
        time = 0
        r = len(grid)
        c = len(grid[0])
        queue = deque()

        fresh = 0

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        while queue and fresh > 0:
            q_len = len(queue)
            for i in range(q_len):
                row, col = queue.popleft()
                for direction in directions:
                    new_row = direction[0] + row
                    new_col = direction[1] + col
                    if new_row < r and new_row >= 0 and new_col < c and new_col >= 0:
                        if grid[new_row][new_col] == 1:
                            queue.append((new_row, new_col))
                            grid[new_row][new_col] = 2
                            fresh -= 1

            time += 1


        if fresh > 0:
            return -1
        return time



            
                    