class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        dp = {} #for a cell it says the max path it took to get here

        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        def dfs(r, c, prev):
            if r < 0 or r > rows - 1:
                return 0 
            if c < 0 or c > cols - 1:
                return 0 
            if matrix[r][c] <= prev:
                return 0

            

            if (r, c) in dp:
                return dp[(r, c)]

            result = 1
            for direction in directions:
                result = max(result, 1 + dfs(r + direction[0], c + direction[1], matrix[r][c]))

            dp[(r, c)] = result
            return result

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, float('-inf'))

        return max(dp.values())


