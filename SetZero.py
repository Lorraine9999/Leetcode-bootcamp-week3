class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        first_row_has_zero = False
        first_col_has_zero = False

        # Step 1: Check if the first row has any zero
        for j in range(n):
            if matrix[0][j] == 0:
                first_row_has_zero = True
                break

        # Step 2: Check if the first column has any zero
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_has_zero = True
                break

        # Step 3: Mark rows and columns
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Step 4: Zero out cells based on marks in the first row and column
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Step 5: Handle the first row
        if first_row_has_zero:
            for j in range(n):
                matrix[0][j] = 0

        # Step 6: Handle the first column
        if first_col_has_zero:
            for i in range(m):
                matrix[i][0] = 0  