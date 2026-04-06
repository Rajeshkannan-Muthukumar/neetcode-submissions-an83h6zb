class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row=set()
        col=set()
        r=len(matrix)
        c=len(matrix[0])
        for i in range(r):
            for j in range(c):
                if matrix[i][j]==0:
                    if i not in row:
                        row.add(i)
                    if j not in col:
                        col.add(j)
        for a in row:
            for j in range(c):
                matrix[a][j]=0
        for b in col:
            for i in range(r):
                matrix[i][b]=0
    
    