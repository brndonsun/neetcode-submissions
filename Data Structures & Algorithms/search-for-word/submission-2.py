class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])
        path = set()

        seen_letters = {}
        def dfs(r, c, i):
            if i == len(word):
                return True

            if r not in range(row) or c not in range(col):
                return False
            if board[r][c] != word[i]:
                return False
            if (r, c) in path:
                return False

            path.add((r, c))
            res = dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) or dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1)
            path.remove((r,c))
            return res

        for r in range(row):
            for c in range(col):
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True

        return False