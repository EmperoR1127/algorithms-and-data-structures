def n_queens(n):
    """Return the solutions of n queens in n*n boards"""

    # ---------- nonpublic utilities ----------
    def _helper(selectedColumns, row, n):
        """selectedColumns: the num of columns selected so far
        row: the row under consideration
        """
        if len(selectedColumns) == n: # find a solution
            print(_print_queens(selectedColumns, n))
            #print(selectedColumns)
            return

        for col in range(n):
            if _is_valid(selectedColumns, col, n): # choose a valid column
                selectedColumns.append(col) # add to the selected columns
                _helper(selectedColumns, row + 1, n) # consider the next row
                selectedColumns.pop() # backtrack

    def _is_valid(selectedColumns, column, n):
        """Check whether the newly selected position is valid
        selectedColumns: the num of columns selected so far
        column: newly selected column
        n: the total num of columns
        """
        for col in selectedColumns:
            if col == column: # column has already been selected
                return False
        top_left, top_right = column - 1, column + 1
        row = len(selectedColumns) - 1 # start from the last selected row
        while (top_left >= 0 or top_right < n) and row >= 0:
            if top_left >= 0:
                if selectedColumns[row] == top_left: # the counter diagonal has been selected 
                    return False
                else:
                    top_left -= 1
            if top_right < n:
                if selectedColumns[row] == top_right: # the digonal has been selected
                    return False
                else:
                    top_right += 1
            row -= 1 # upward iteration

        return True

    def _print_queens(selectedColumns, n):
        """Print the board with a valid solution"""
        res = []
        for i in range(n):
            row = ["*" for _ in range(n)]
            row[selectedColumns[i]] = "Q" # only one queen in each row
            res.append("".join(row))
            res.append("\n")
        return "".join(res)

    print("The valid solutions of {0} queens problems in a {0} * {0} board are: ".format(n))
    _helper([], 0, n)


if __name__ == "__main__":
    n_queens(4)













        
        
        
