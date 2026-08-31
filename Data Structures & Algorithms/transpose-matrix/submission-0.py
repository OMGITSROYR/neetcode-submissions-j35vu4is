class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ROW = len(matrix)
        COLS = len(matrix[0])
        res = [[0] * ROW for _ in range(COLS)]

        for i in range(ROW):
            for j in range(COLS):
                res[j][i] = matrix[i][j]

        return res