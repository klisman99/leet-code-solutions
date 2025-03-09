class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        columns = [{} for _ in range(9)]
        rows = [{} for _ in range(9)]
        quadrants = [{} for _ in range(9)]

        for i in range(len(board)):
            for j in range(len(board[i])):
                cell = board[i][j]

                if cell == ".": continue

                if rows[i].get(cell, 0) == 0:
                    rows[i][cell]  = 1
                else:
                    return False

                if columns[j].get(cell, 0) == 0:
                    columns[j][cell]  = 1
                else:
                    return False
                
                quadrant = 3 * (i // 3) + (j // 3)

                if quadrants[quadrant].get(cell, 0) == 0:
                    quadrants[quadrant][cell]  = 1
                else:
                    return False

        return True