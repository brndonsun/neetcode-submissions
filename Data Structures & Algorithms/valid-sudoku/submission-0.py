class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_hash = {}
        col_hash = {}
        rows = len(board)
        cols = len(board[0])

        #row checking
        for r in range(rows):
            row_hash = {}
            for c in range(cols):
                if board[r][c] == ".": continue
                if board[r][c] in row_hash.keys():
                    return False
                row_hash[board[r][c]] = 1

        #column checking
        for c in range(cols):
            col_hash = {}
            for r in range(rows):
                if board[r][c] == ".": continue

                if board[r][c] in col_hash.keys():
                    return False
                col_hash[board[r][c]] = 1

        # 9x9 checking
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        return True



