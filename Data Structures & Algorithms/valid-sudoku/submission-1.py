from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_map = defaultdict(set)
        col_map = defaultdict(set)
        square_map = defaultdict(set)

        for row in range(len(board)):
            for col in range(len(board)):
                value = board[row][col]
                if value == '.':
                    continue
                square = (row // 3) * 3 + (col // 3)
                if value in row_map[row] or value in col_map[col] or value in square_map[square]:
                    return False
                # Each of the maps below will append the value of the index they hold in a list
                row_map[row].add(value)
                col_map[col].add(value)
                square_map[square].add(value)
        return True

                