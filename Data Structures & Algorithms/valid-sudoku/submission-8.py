class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(0,9):
            rowset=set()
            for i in range(0,9):
                if board[row][i]!="." and board[row][i] in rowset:
                    return False
                elif board[row][i]!=".":
                    rowset.add(board[row][i])
        for col in range(0,9):
            colset=set()
            for j in range(0,9):
                if board[j][col] !="." and board[j][col] in colset:
                    return False
                elif board[j][col] !=".":
                    colset.add(board[j][col])
        def helper(r,c):
            b=set()
            for i in range(r,r+3):
                for j in range(c,c+3):
                    if board[i][j]!="." and board[i][j] in b:
                        return False
                    elif board[i][j]!=".":
                        b.add(board[i][j])
            return True
        for z in range(0,9,3):
            for k in range(0,9,3):
                if not helper(z,k):
                    return False
        return True

            




        