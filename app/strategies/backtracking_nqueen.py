class BacktrackingNQueensSolver:
    
    def __init__(self, n):
        self._solutions_founded = []
        self.n = n
    

    def find_all_solutions(self):
        rows_array = []
        self._solutions_founded = []
        self._nqueen(1, rows_array)
        return self._solutions_founded.copy()
    
    
    def _is_queen_safe(self, row_pos, column_pos, rows_array):
        col = 1
        for row in rows_array:
            columns_diff = abs(col - column_pos)
            rows_diff = abs(row - row_pos)
            if columns_diff == rows_diff:
                return False
            col += 1
        return True
    

    def _nqueen(self, row, rows_array):
        if row > self.n:
            self._solutions_founded.append(rows_array.copy())
            return
        for i in range(1, self.n+1):
            if i not in rows_array and self._is_queen_safe(i, len(rows_array) +1, rows_array):
                rows_array.append(i)
                self._nqueen(row+1, rows_array)
                rows_array.pop()

