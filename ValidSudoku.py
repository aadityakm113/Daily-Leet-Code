# https://leetcode.com/problems/valid-sudoku/
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #create dictionaries with default values of an empty hashset for rows,cols and squares
        cols=collections.defaultdict(set)
        rows=collections.defaultdict(set)
        squares=collections.defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                #check if position is empty
                if board[r][c]==".":
                    continue
                #check if value is a duplicate. Check if it is already present in our hashsets
                if (board[r][c] in cols[c] or
                    board[r][c] in rows[r] or
                    board[r][c] in squares[(r//3,c//3)] ):
                    return False
                #update sets
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3,c//3)].add(board[r][c])
        return True
                