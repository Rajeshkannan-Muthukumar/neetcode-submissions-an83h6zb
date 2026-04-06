class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res=[]
        l=0
        r=len(matrix[0])-1
        u=0
        d=len(matrix)-1
        while u <= d and l <= r:
            for i in range(l,r+1):
                if u<=d:
                    res.append(matrix[u][i])
            u+=1
            for j in range(u,d+1):
                if l<=r:
                    res.append(matrix[j][r])
            r-=1
            for k in range(r,l-1,-1):
                if u<=d:
                    res.append(matrix[d][k])
            d-=1
            for z in range(d,u-1,-1):
                if l<=r:
                    res.append(matrix[z][l])
            l+=1
        return res