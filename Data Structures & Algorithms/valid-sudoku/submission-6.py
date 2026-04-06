class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def rchecker(board,r):
            row=set()
            for j in range(9):
                if board[r][j] != "." and board[r][j] not in row:
                    row.add(board[r][j])
                elif board[r][j] !="." and board[r][j] in row:
                    return False
            return True
        def cchecker(board,c):
            col=set()
            for i in range(9):
                if board[i][c] != "." and board[i][c] not in col:
                    col.add(board[i][c])
                elif board[i][c] !="." and board[i][c] in col:
                    return False
            return True
        def gridcheck(board,r,c):
            grid=set()
            for i in range(r,r+3):
                for j in range(c,c+3):
                    if board[i][j] != "." and board[i][j] not in grid:
                        grid.add(board[i][j])
                    elif board[i][j] !="." and board[i][j] in grid:
                        return False
            return True
        flag=True
        num=(0,3,6)
        for i in range(9):
            for j in range(9):
                if i in num and j in num:
                    flag = rchecker(board,i) and cchecker(board,j) and gridcheck(board,i,j)
                else:
                    flag = rchecker(board,i) and cchecker(board,j)
                if not flag:
                    return flag
        return flag

            




        