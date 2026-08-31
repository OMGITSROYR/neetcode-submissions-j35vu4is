class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ROWS = len(mat)
        COLS = len(mat[0])
        res = 0

        for i in range(ROWS):
            res += mat[i][i]
            if i != COLS -1 -i:
                res += mat[i][COLS -1 -i]
        return res