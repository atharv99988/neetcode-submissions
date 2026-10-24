class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # variable to make column 1 to zeros if there is a column
        col = 1
        ROWS = len(matrix)
        COLUMNS = len(matrix[0])

        for r in range(ROWS)  :
            for c in range(COLUMNS) : 
                if matrix[r][c] == 0:
                    if c == 0:
                        col = 0
                    else:
                        matrix[r][0] = 0
                        matrix[0][c] = 0

        for r in range(1, ROWS) :
            for c in range(1, COLUMNS) : 
                if matrix[0][c] == 0 or  matrix[r][0] == 0 : 
                    matrix[r][c] = 0 

        if matrix[0][0] == 0 : 
            for c in range(COLUMNS) : 
                matrix[0][c] = 0
        
        if col == 0 :
            for r in range(ROWS) : 
                matrix[r][0] = 0

        



        
        