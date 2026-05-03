class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        #initialize chess board:
        res = []
        board = []
        marked_col = set()
        marked_diag1 = set()  # stores r - c values
        marked_diag2 = set()  # stores r + c values

        row_str = ""
        for i in range (n):
            row_str += '.'

        for i in range (n):
            board.append(row_str)

        def backtrack(row):

            
            if row == n:
                res.append(board.copy())
                return

            #check next row 
            for col in range(n):
                    #you're in a row or column where a queen already exists
                if (((col in marked_col)) or
                ((row - col) in marked_diag1) or                
                ((row + col) in marked_diag2)): 
                    continue
                

                char_list = list(board[row])
                char_list[col] = 'Q'
                row_str = "".join(char_list)
                board[row] = row_str

                marked_col.add(col)
                marked_diag1.add(row-col)
                marked_diag2.add(row+col)
            
                #Recurse, then reset changes afterwards
                backtrack(row+1)

                char_list = list(board[row])
                char_list[col] = '.'
                row_str = "".join(char_list)
                board[row] = row_str

                marked_col.remove(col)
                marked_diag1.remove(row-col)
                marked_diag2.remove(row+col)

        backtrack(0)
        return res
            
