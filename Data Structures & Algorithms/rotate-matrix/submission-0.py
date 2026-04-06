class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n=len(matrix)
        m=len(matrix[0])
        for i in range(m):
            for j in range(i):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        
        for i in range(n):
            for j in range(m//2):
                matrix[i][j],matrix[i][m-1-j]=matrix[i][m-1-j],matrix[i][j]
        # return matrix