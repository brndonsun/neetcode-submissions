import math

class Solution:

    def diagonalSum(self, mat: List[List[int]]) -> int:
        result = 0
        for i in range(len(mat)):
            result += mat[i][i]
        for j in range(len(mat)):
            result += mat[j][len(mat) - j - 1]

        if len(mat) % 2 == 1:
            return result - mat[math.floor(len(mat) / 2)][math.floor(len(mat) / 2)]
        else:
            return result

        